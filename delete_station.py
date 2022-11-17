import pprint
import pymongo
import json
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://Saliou:imwcVjBAhIZvwV9n@cluster0.e2aqyh7.mongodb.net/test", server_api=ServerApi('1'))
db = client.vls
def supprime_stations (_id_station):
    """
    supprimer une station par son id dans les deux collections
    """

    db.stations.delete_one( {"_id":_id_station} )

    db.datas.delete_many( {"station_id":_id_station} )
supprime_stations(41)
