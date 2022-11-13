import pprint
import pymongo
import json
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://Saliou:imwcVjBAhIZvwV9n@cluster0.e2aqyh7.mongodb.net/test", server_api=ServerApi('1'))
db = client.vls

def search(station):
    """
    search for a station by name with only some letters or part of the name
    """
    
    cur = db.stations.find({"name": {"$regex":station}})
    liste_nom=[]
    for doc in cur:
        liste_nom.append(doc)
    print(liste_nom)
search("Bu")