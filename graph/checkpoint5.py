import random
import time
import datetime
from pymongo import MongoClient
client = MongoClient()
db = client.csci2963
count = db.definitions.count()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    rnum = random.randint(0,count-1)
    record = db.definitions.find().limit(-1).skip(rnum).next()
    time = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    db.definitions.update(
        {"word" : record["word"]},
        {"$push" : {"dates": time}}
    )
    print record
    return record, record["word"]

if __name__ == '__main__':
    print("first access the entry\n")
    a = random_word_requester()
    print("\nafter inserted time, access the word again\n")
    for post in db.definitions.find({"word":a[1]}):
        print post