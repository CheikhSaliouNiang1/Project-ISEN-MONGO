import pprint
import pymongo
import json
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
import run
client = MongoClient("mongodb+srv://Saliou:imwcVjBAhIZvwV9n@cluster0.e2aqyh7.mongodb.net/test", server_api=ServerApi('1'))
db = client.vls
def update_station (station):
    datas = run.get_vlille()
    data = {}
    _id = {}

    for i in datas:
        if i["name"] == station:
            data = i
            _id["_id"] = data.pop("_id",None)

    try:
        db.stations.update_one(_id, {"$set": data}, upsert = True)
        return True
    except:
        return False
update_station("Buisson")