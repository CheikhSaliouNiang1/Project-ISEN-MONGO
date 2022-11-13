import pprint
import pymongo
import json
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://Saliou:imwcVjBAhIZvwV9n@cluster0.e2aqyh7.mongodb.net/test", server_api=ServerApi('1'))
db = client.vls
def deactivate_zone(lat, lon, dist):
    """
    deactivate all stations in a select area
    """
    # filtre nearby dans global
    found= db.stations.find({"geometry": 
                                   {"$near": 
                                    {"$geometry":
                                     {"type": "Point",
                                      "coordinates": [lat, lon]},
                                                     "$maxDistance": dist}}, "Available":"True"})
    
    for i in found:

    
        desac=db.stations.update_one({"_id":i["_id"]}, {"$set": {"Available": "False"}},
                                  upsert = True)
    
deactivate_zone(3.071121,50.637171,10000)