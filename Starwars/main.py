# TASK INSTRUCTIONS
# The data in this database has been pulled from https://swapi.dev/. As well as 'people', the API has data on starships.
# In Python, pull data on all available starships from the API.
# The 'pilots' key contains URLs pointing to the characters who pilot the starship.
# Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection.
# Use functions at the very least!

# LIBS
# ------------
# Requests library for HTTP requests to APIs
import pymongo
# Pymongo library for accessing NoSQL/MongoDB database(s)
import requests
from pprint import pprint

# Function which is used to add the ships received from the
# api call to the database
def add_into_database(api_starwars):
    db["starships"].insert_many(ships_from_swapi(api_starwars))

# Function that returns the number of ships received from the api call
def ships_from_swapi(api_starwars):
    ships_list = []
    while api_starwars["next"] != None:
        # Loop through the ships list and add them to an empty list
        for each_ship in api_starwars["results"]:
            ships_list.append(each_ship)
        # If there are no more ships left, break out of
        # Set a new variable to go to the next page and continue
        new_page = requests.get(api_starwars["next"])
        api_starwars = new_page.json()
    # if "next" is equal to None, then loop throught the ships left and add them to the empty list
    if api_starwars["next"] == None:
        for each_ship in api_starwars["results"]:
            ships_list.append(each_ship)
    # pprint(ships_list)
    return ships_list

# Function which is  accessing the pilot name from the database
def get_pilot_name(pilot):

    pilot_api = requests.get(pilot)
    pd = pilot_api.json()
    return pd["name"]

# Function which to return the pilot ids and
# to update the entries in the database
def get_pilots(database):
    pilots_ids = []
    # loop through the list of pilots in the database
    for pilot in database:
        if pilot["pilots"]:
            ids = []
            # loop through each pilot and find the coresponding id from the character database
            for each_pilot in pilot["pilots"]:
                # get the pilot name
                pilot_name = get_pilot_name(each_pilot)
                # get the pilot id
                pilot_id = db.characters.find({"name": pilot_name}, {"_id": 1})
                # loop through the pilot_ids
                for each_id in pilot_id:
                    # append the ids and the pilots_ids
                    ids.append(each_id["_id"])
                    pilots_ids.append(each_id["_id"])
                    # update the mongo database with the new pilot ids
                    db.starships.update_one({"_id": pilot["_id"]}, {"$set": {"pilots": ids}})
    return pilots_ids

# Initialise Pymongo client
client = pymongo.MongoClient()
# Connect to database with the supplied name
db = client['starwars']
# The following operation drops the starships collection in the current database.
db.starships.drop()

if __name__ == '__main__':
    swapi = requests.get("https://swapi.dev/api/starships/?page=1")
    swapi_api_ships = swapi.json()

    add_into_database(swapi_api_ships)

    pilots = db.starships.find()

    get_pilots(pilots)

