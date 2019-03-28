#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, request, report
import requests
from pymongo import MongoClient

connection = MongoClient('locolhost', 27017)
db = connection['city']
collection = connection['inspections']


def create_document():
  myDocument = {"company" : "ACME RoadRunner Traps", "address" : "1313 Mockingbird lane"}
  x = mycol.insert_one(myDocument)
  if (insert_one = true):
    return print(x.inserted_id)
  else:
    print("no id created for document")

def insert_document(document):

  try:
    result=collection.save(document)
    except ValidationError as ve:
      abort(400, str(ve))
      return result

def get_document(key, value):
    document = collection.find_one({key:value})
    if not document:
        abort(404, 'No document with %s : %s' % key,value)

     return document
     
def update_document(key, value,document):

       result = collection.update({key:value},{ '$set': document }, upsert=False,multi=False) 

       if not result:

                 abort(404, 'No document with %s : %s' % key,value)

       return json.loads(json.dumps(result, indent=4, default=json_util.default))
       
def delete_document(key, value):

      result = collection.delete_one({key:value})

      if not result:

                abort(404, 'No document with %s : %s' % key,value) 

      return result
      
def update_document(key, value,document):
      result = collection.update({key:value},{ '$set': document }, upsert=False,multi=False) 
      if not result:
             abort(404, 'No document with %s : %s' % key,value) 
      return json.loads(json.dumps(result, indent=4, default=json_util.default)) 

@url('/name/<params>', method='GET')
def text_show( name="Hellow World"):
  return name

@url('/name/<params>', method='DELETE')
def text_delete( name="Hello World"):
  return "DELETE" + name

@url('/name/<params>', method'PUT')
def text_put( name="Hello World"):
  return "Saved" + name

@url('/name/<params>', method'UPDATE')
def text_update(name = "Hello World"):
  return "Updated" + name
myClient = http://localhost/hello?name=”world"
curl -x GET http://localhost/hello?name="world"
curl -x DELETE http://localhot/hello?name="world"
curl -x PUT http://localhost/hello?name="world" 
curl -x UPDATE http://localhost/hello?name="world"
PARAMS = {hello : "world"}

current_date_time = datetime.datetime.now() # it will give current system date and time
print (current_date_time)

# pass url for your mongo here bydefault will be taking localhost:27017 default port for mongoDB
myClient = MongoClient()

# pyDatabase is your database name you can access it like myClient["pyDatabase"] this also.
db = myClient.pyDatabase

users = db.users # users is collection name where your want to insert data.

# indexing
db.users.create_index([("name", pymongo.ASCENDING)],unique = True)

# single Insert
user1 = {curl -H "Content-Type: application/json" -X POST -d   '{"id" : "10011-2017-TEST","certificate_number" : 9278833,"business_name" : “ACME TEST INC.","date" : "Feb 20 2017","result" : "No Violation Issued","sector" : "Test Retail Dealer - 101"}' http://localhost:8080/create:current_date_time}
user_id = users.insert_one(user1).inserted_id
print (user_id)

print (UsersObj.find().count())
print (UsersObj.find({"name":"vivek"}).count())
print (UsersObj.find())

old_date = datetime.datetime(2019, 2 , 17)



print (UsersObj.find({"createdDate": {"$gte": old_date}}).count())

# $exists used when you want to check if collection data has this columns or not as its nosql
# so it might possible that column should not be there for some data
print (UsersObj.find({"likes": {"$exists": True}}).count())

def create_document(key, value, document):
  result = collection.update({key:value},{'$set':document},upsert=False,multi=False)
  if result:
     print document{key:value}
     return json.loads(json.dump(result, indent=4, default=json_util.default)

@route('/create', method='POST')
def create():
      tickerSymbol = "ACME"
      get.url("http://ACME/stocks/api/v1.0/createStock/ACME")
      entity=get_document(request.query.tickerSymbol.result)
                       
def read_document(key, value, document):
  result = collection.read({key:value},{'$set':document},upsert=False,multi=False)
  if not entity:
              abort(404, 'update erro %s' % request.query.result)
  if result:
     print(document + "200 OK")
     print document{key:value}
     return json.loads(json.dump(result, indent=4, default=json_util.default)

@route('/get', method='POST')
def create():
      tickerSymbol = "ACME"
      get.url("http://ACME/stocks/api/v1.0/createStock/ACME")
      entity=get_document(request.query.tickerSymbol.result)
      if not entity:
              abort(404, 'update erro %s' % request.query.result)
      else:
              print("200 OK")
      return json.companies.tickerSymbol

@route('/read', method='GET') 
def update():
      old_doc = get_document("id",request.query.id) 
      entity=update_document(request.query.id,request.query.result,old_doc) 
      if not entity: 
             abort(404, 'update error %s' % request.query.result)
      return json.loads(json.dumps(entity, indent=4, default=json_util.default)) 

                       
@route('/delete', method='GET') 
def update(): 
        entity=delete_document("id",request.query.id) 
        if not entity: 
                  abort(404, 'delete error %s' % request.query.id)
        return json.loads(json.dumps(entity, indent=4, default=json_util.default)) 
        

        
@route('/documents', method='PUT')
def put_document():
    data = request.url.readline()
    print(data)
    if not data:
        abort(404, 'Not found')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db.documents.insert(entity)
    except ValidationError as ve:
        abort(400, str(ve))
        
    if found:
    return print('200 ok')
    
    if insert_document:
    print('201 Created')

@route('/update', method='POST')
def post(id, name):
      entity=post_document("id", request.query.company.id)
      while(entity.count < 4: entity = 0: ++entity.id:)
      print(entity.url)
      if not entity:
                abort(404, 'stock price %s not listed' % request.query.company.id)
      else:
        print("200 ok")
      return entity.list
      

    
