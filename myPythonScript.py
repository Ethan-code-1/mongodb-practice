from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/sample_restaurants"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

db = client.ebo4dq 
collection = db.labNine


record_one = {
    "name" : "Lionel Messi",
    "age" : 36,
    "teams" : [
        "Inter Miami",
        "PSG",
        "FC Barcelona"
        ]
}

record_two = {
    "name" : "Cristiano Ronaldo",
    "age" : 39,
    "teams" : [
        "Al-Nassr",
        "Sporting",
        "Real Madrid",
        "Manchester United"
        ]
}


record_three = {
    "name" : "Kylian Mbappe",
    "age" : 25,
    "teams" : [
        "Monaco",
        "PSG"
        ]
}

record_four = {
    "name" : "Neymar Junior",
    "age" : 32,
    "teams" : [
        "FC Barcelona",
        "PSG",
        "Al Hilal"
        ]
}

record_five = {
    "name" : "Erling Haaland",
    "age" : 23,
    "teams" : [
        "Dortmund",
        "Manchester City"
        ]
}

documentsToInsert = [record_one, record_two, record_three, record_four, record_five]
collection.insert_many(documentsToInsert)

#Writing query to show exactly three documents: Find all players that played for PSG (3)

threeRecords = collection.find({"teams" : "PSG"})
print(dumps(threeRecords, indent = 2))