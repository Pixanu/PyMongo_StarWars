import pymongo
import requests
from pprint import pprint


#--------------------------
#--------------------------
#Test pymongo and request
req = requests.request('GET', 'https://httpbin.org/get')
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r)

client  = pymongo.MongoClient()
db=client['starwars']

luke = db.characters.find_one({"name": "Luke Skywalker"})
pprint(luke)
