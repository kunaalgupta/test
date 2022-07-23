import pymongo
client = pymongo.MongoClient("mongodb+srv://JR-Test:qwer1234@test.dactg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["myinfo"]
collection = database["kunal"]

record = collection.find()
for i in record:
    if "product" in i.keys():
        print(i)
print("=====================================")
data=collection.find({"companyName":"iNeuron"})
for i in data:
    print(i)

print("=====================================")
data = collection.find({"courseOffered":{"$gt":"E"}})
for i in data:
    print(i)