import pymongo


client = pymongo.MongoClient("10.99.70.37", 27017)

print(client)
print(client.database_names())

db = client.bian

print(db)
print(db.name)

collection = db.biancollection1
print(collection)

# collection.create_index('x')

one = {
    'x': 12
}
# collection.insert_one(one)

# print(collection.find_one())

for item in collection.find():
    print(item)
print()


for item in collection.find().sort('x', pymongo.ASCENDING):
    print(item)
print()

print([item for item in collection.find().limit(3).skip(3)])