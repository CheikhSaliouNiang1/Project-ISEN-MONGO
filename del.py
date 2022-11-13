import pprint
import pymongo
import json
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://Saliou:imwcVjBAhIZvwV9n@cluster0.e2aqyh7.mongodb.net/test", server_api=ServerApi('1'))
db = client.vls
def delete_station_datas (_id_station):
    """
    delete a station by "_id" in "stations" and all the corresponding records in 'datas'
    """

    db.stations.delete_one( {"_id":_id_station} )

    db.datas.delete_many( {"station_id":_id_station} )
delete_station_datas(41)
