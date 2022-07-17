import pymongo
client = pymongo.MongoClient("mongodb+srv://kunaalgupta:qwer1234@cluster0.wyztm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Kunal",
    "surname":"Gupta",
    "email":"kunal@123"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
