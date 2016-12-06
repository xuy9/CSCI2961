from pymongo import MongoClient
client = MongoClient()
db = client.csci2963

if __name__ == '__main__':
    print ("all definitions")
    for post in db.definitions.find():
        print post
    a = db.definitions.find_one()
    print ("one definition")
    print a

    db.definitions.insert({"word":"bonjour", "definition":"Hello in French"})
    for post in db.definitions.find({"word":"Blow Off"}):
        print post
    for post in db.definitions.find({"_id": "ObjectId('56fe9e22bad6b23cde07b8c8')"}):
        print post