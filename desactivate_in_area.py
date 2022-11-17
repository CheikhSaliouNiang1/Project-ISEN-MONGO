import pprint
import pymongo
import json
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://Saliou:imwcVjBAhIZvwV9n@cluster0.e2aqyh7.mongodb.net/test", server_api=ServerApi('1'))
db = client.vls
def zone_desactivation(lat, lon, dist):
    """
    désactivation de stations dans une zone
    """
    # filtre nearby dans stations
    found= db.stations.find({"geometry": 
                                   {"$near": 
                                    {"$geometry":
                                     {"type": "Point",
                                      "coordinates": [lat, lon]},
                                                     "$maxDistance": dist}}, "Available":"True"})
    
    for i in found:

    
        desac=db.stations.update_one({"_id":i["_id"]}, {"$set": {"Available": "False"}},
                                  upsert = True)
    
zone_desactivation(3.071121,50.637171,10000)
