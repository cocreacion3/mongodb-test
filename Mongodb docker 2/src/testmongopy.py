import pymongo
from pymongo import MongoClient

MONGO_URI = "mongodb://mongodb:27017/"
MONGO_TIME_OUT = 1000


try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT)
    # client.server_info()
    print("connection successful")

    db = client['maga'] #new db
    collection = db['devices'] #new collection

    # collection.insert_one({"_id":1, "name":"MAGA001"}) #only inser one document

    # maga_one = {"_id":3, "name":"MAGA003"}
    # maga_two = {"_id":4, "name":"MAGA004"}
    # collection.insert_many([maga_one, maga_two]) #insert many documents

    # collection.update_one({"_id":1}, {"$set": {"name":"newMAGA001"}}) #update document
    collection.update_one({"_id":1}, {"$set": {"id":8}})


    print("RESULT----------------------------------")
    results = collection.find()
    for result in results:
        print(result)
    print("----------------------------------------")

    # collection.delete_many({})


    client.close()

except pymongo.errors.ServerSelectionTimeoutError as error:
    print("Timeout")
    pass
except pymongo.errors.ConnectionFailure as errorConnection:
    print("Connection failure")


print("end")
exit()
