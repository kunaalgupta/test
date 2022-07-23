import pymongo
client = pymongo.MongoClient("mongodb+srv://JR-Test:qwer1234@test.dactg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Kunal",
    "surname":"Gupta",
    "email":"kunal@123"
}
d1 = {
    "name":"Ram",
    "surname":"Sharma",
    "email":"ram_sharma@123"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
coll.insert_one(d1)
coll.delete_one(d)

