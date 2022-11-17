import pprint
import pymongo
import json
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://Saliou:imwcVjBAhIZvwV9n@cluster0.e2aqyh7.mongodb.net/test", server_api=ServerApi('1'))
db = client.vls

def recherche(station):
    """
    Trouver une station par son nom ou juste par quelques lettres grace aux expression régulière
    """
    
    found = db.stations.find({"name": {"$regex":station}})
    liste_nom=[]
    for i in found:
        liste_nom.append(i)
    print(liste_nom)
recherche("Bu")
