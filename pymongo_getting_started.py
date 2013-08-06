import pymongo

#from pymongo import Connection
#connection = Connection('localhost', 27017)
# After pymongo 2.4

from pymongo import MongoClient
connection=MongoClient()

db =connection.test

names =db.names

item = names.find_one()

print item['name']
