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
     db["starships"].insert_many(api_starwars)

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
         # function is not returning last page
     # find a way to acces the last page and return the ships_list



client = pymongo.MongoClient()
db = client['starwars']


swapi = requests.get("https://swapi.dev/api/starships/?page=1")
swapi_api_ships = swapi.json()
pprint(swapi_api_ships)


# --------------------------------------------
# TESTING to see if the api goes to the next page
# new_page = requests.get(swapi_api_ships["next"])
# test_page = new_page.json()
# pprint(test_page)


#add_into_database(swapi_api_ships)