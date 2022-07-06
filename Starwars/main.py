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

def add_into_database(api_starwars):
     db["starships"].insert_many(ships_from_swapi(api_starwars))

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
     #pprint(ships_list)
     return ships_list



def get_pilots(database):
     pilots_ = []
     # loop through the list of pilots in the database
     for pilot in database:
          #for each pilot in pilots do a api requests and append it to the list
          for each_pilot in pilot["pilots"]:
               pilot_api = requests.get(each_pilot)
               pilot_json = pilot_api.json()
               pilots_.append(pilot_json)

     pprint(pilots_)
     return pilots_




client = pymongo.MongoClient()
db = client['starwars']


swapi = requests.get("https://swapi.dev/api/starships/?page=1")
swapi_api_ships = swapi.json()
# pprint(swapi_api_ships)

add_into_database(swapi_api_ships)

pilots = db.starships.find()

get_pilots(pilots)



# --------------------------------------------
# TESTING to see if the api goes to the next page
# new_page = requests.get(swapi_api_ships["next"])
# test_page = new_page.json()
# pprint(test_page)


