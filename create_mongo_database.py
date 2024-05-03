import pymongo
import csv

with open("Dataset/Plant_1_Generation_Data.csv", 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

with open("Dataset/Plant_2_Generation_Data.csv", 'r') as file:
    reader_1 = csv.DictReader(file)
    data_1 = list(reader_1)

client = pymongo.MongoClient()
db = client['sensor_database']
collection = db['sensor_collection']
collection.delete_many({})

for row in data:
    collection.insert_one(row)
for row_1 in data_1:
    collection.insert_one(row_1)

client.close()