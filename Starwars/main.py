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




# def add_into_database(api_starwars):
#     db["starships"].insert_many(api_starwars)


client = pymongo.MongoClient()
db = client['starwars']


swapi = requests.get("https://swapi.dev/api/starships")
swapi_api_ships = swapi.json()
pprint(swapi_api_ships)

#add_into_database(swapi_api_ships)