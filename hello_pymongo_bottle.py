import bottle
import pymongo

#this is the handler for the root address of the web server
@bottle.route('/')
def index():
   from pymongo import Connection
   connection=Connection('localhost',27017) # get a connection to the database server

   db =connection.test # attached to test database

   names =db.names  # get a handle for the names collection

   item =names.find_one() or "hello"  # find a sginle item from names

   return '<b>Hello %s!<b>' % item['name'] 

bottle.run(host='localhost',port=8082)
