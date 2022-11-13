from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

############################# Appel de la base donnee ############################# 

client = MongoClient("mongodb+srv://azynux:Km3pP>_n5W{6@cluster0.ayrjn7t.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.vls

print("\n")
latA = float(input("Veuillez entrer votre latitude: "))
longA = float(input("Veuillez entrer votre longitude: "))

############################# Creation des variables pour faciliter l'utilisation de la base de donnée ############################# 

database = client["vls"] # base de donnée
stations = database["stations"] # collection stations
datas = database["datas"] # collection datas

############################# Recuperation des id proches de l'utilisateur dans un rayon defini dans la collection stations ############################# 

query = {}

query["geometry.coordinates"] = {
    u"$near": {
        u"$geometry": {
            u"type": u"Point",
            u"coordinates": [
                longA,
                latA
            ]
        },
        u"$maxDistance": 500.0,
        u"$minDistance": 0.0
    }
}

projection = {}
projection["_id"] = 1.0
projection["name"] = 1.0

cursor = stations.find(query, projection = projection)
K = list(cursor)
id = []
for i in range(0,len(K)):
    id.append(K[i]["_id"])

############################# Filtrage des id dans la collections datas pour recuperer les stand et les velo proches ############################# 

query = {}
query["station_id"] = {
    u"$in": id
}

projection = {}
projection["_id"] = 0.0
projection["date"] = 0.0
sort = [ (u"date", -1) ]

cursor = datas.find(query, projection = projection, sort = sort, limit = len(id))
resultat = list(cursor)

############################# Station de vélo avec le nombre de vélos et de stands disponible ############################# 

velo = []

for i in range(0,len(K)):
    for j in range(0,len(resultat)):
        if K[i]["_id"] == resultat[j]["station_id"] : 
            velo.append(K[i]['name'])
            velo.append(resultat[j]['bike_availbale'])
            velo.append(resultat[j]['stand_availbale'])


i = len(velo)
b = 3
k = 0

while(i != 0):
  print("\n")  
  print("####################################") 
  a = velo[k:b]
  i -= 3
  b += 3
  k += 3
  print("Nom de la station:", a[0],"\nVélo disponible:", a[1],"\nStand disponible: ", a[2])

print("\n")