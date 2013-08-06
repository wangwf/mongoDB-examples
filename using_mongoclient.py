
#
# AFter  MongoDB 2.4,  using MongoClient instead of connection
#
import pymongo
#from pymongo import MongoClient

c = pymongo.MongoClient(host="mongodb://localhost:27017",w=1,j=True)
db = c.m101

people =db.people

people.remove({})

print "inserting"

#people.insert({"name":"Wenfeng Wang","favorite_color":"green"})
#people.insert({"name":"Wenfeng","favorite_color":"blue"})
#people.insert({"name":"Wang","favorite_color":"red"})
people.save({"name":"Wenfeng Wang","favorite_color":"green"})
people.save({"name":"Wenfeng","favorite_color":"blue"})
people.save({"name":"Wang","favorite_color":"red"})

print "find_one"
print people.find_one()

print "item"
for item in people.find():
    print item


import datetime
post = {"name": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

people.insert(post)

print [item["name"] for item in db.people.find().sort("name", pymongo.ASCENDING)]

db.people.create_index("name")
for item in db.my_collection.find().sort("name", pymongo.ASCENDING):
     print item["name"]
