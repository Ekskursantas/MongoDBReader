import pymongo
from pymongo import MongoClient
from operator import attrgetter
client = MongoClient()


db = client.social_net
answer = db.tweets.find()
def GetAllUniqueUsers():
    print(len(db.tweets.distinct("user")))

def GetMostLinkingUsers():
    pipeline = [
        {'$match':{'text':{'$regex':"@\w+"}}},
        {'$addFields': {"mentions":1}},
        {'$group':{"_id":"$user", "mentions":{'$sum':1}}},
        {'$sort':{"mentions":-1}},
        {'$limit':10}]
    cursorlist = db.tweets.aggregate(pipeline)
    for cursor in cursorlist:
        print(cursor)
    
def GetMostLinkedUsers():
    pipeline = [
        {'$addFields': {'words': {'$split': ['$text', ' ']}}},  # split text
        {'$unwind': "$words"},  # reconstruct an array of words
        {'$match': {'words': {'$regex': "@\w+", '$options': 'm'}}}, # match the @ from the words list
        {'$group': {'_id': "$words", 'total': {'$sum': 1}}},
        {'$sort': {'total': -1}},  # sort the total
        {'$limit': 5},
    ]
    tweets = db.tweets.aggregate(pipeline)
    for tweet in tweets:
        print(tweet)


def GetMostActiveUser():
    pipeline = [
        {'$group': {'_id': "$user", 'total': {'$sum': 1}}},
        {'$sort': {'total': -1}},
        {'$limit': 10},
    ]
    users = db.tweets.aggregate(pipeline)
    for user in users:
        print(user)


def GetMostNegativeTweets():
    
    pipeline = [
        {'$match':{'text': {'$regex':'pissed|mad|angry|sad|furious|outraged','$options':'g'}}},
        {'$group':{'_id':"$user", 'emotion': {'$avg':"$polarity"}, 'total_negative_tweets': {'$sum': 1}}},
        {'$sort':{ 'emotion': 1, 'total_negative_tweets':-1}},
        {'$limit':5}
    ]
    negativeUser = db.tweets.aggregate(pipeline)
    for negUser in negativeUser:
        print(negUser)

def GetMostPositiveTweets():
    pipeline = [
        {'$match':{'text': {'$regex':'happy|excited|great|amazing|love|enticed','$options':'g'}}},
        {'$group':{'_id':"$user", 'emotion': {'$avg':"$polarity"},'total_positive_tweets': {'$sum': 1}}},
        {'$sort':{ 'emotion': -1, 'total_positive_tweets':-1}},
        {'$limit':5}
    ]
    positiveUser = db.tweets.aggregate(pipeline)
    for posUser in positiveUser:
        print(posUser)

       
print("Get Total Number Of Unique Users")
GetAllUniqueUsers()
print("Get Most Linking Users:")
GetMostLinkingUsers()
print("Get Most Linked Users:")
GetMostLinkedUsers()
print("Get Most Active Users:")
GetMostActiveUser()
print("Get The Happiest Users:")
GetMostPositiveTweets()
print("Get The Saddest Users:")
GetMostNegativeTweets()
