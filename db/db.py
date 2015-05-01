import pymongo, json

MONGODB_URI = 'mongodb://parser:parser@ds049661.mongolab.com:49661/class-swap'

def get_db():
    client = pymongo.MongoClient(MONGODB_URI)
    db = client['class-swap']
    return db

def get_courses():
    return get_db().courses

def get_listed():
    return get_db().listed

def get_users():
    return get_db().users