Follow the steps to get the database and MongoDB:


Firstly, install Docker:

````wget -O - https://bit.ly/docker-install | bash````

After Docker is installed you need to setup your MongoDB:

```sudo docker run --rm -v $(pwd)/data:/data/db --name dbms --publish=27017:27017 -d mongo:latest```

```sudo docker run -it --link dbms:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'```

After MongoDB container is setup, we finally can use our python script. We locate ourself to the folder where the script is located and the run the syntax:

```python MongoDBReader.py```

It will print out all the answers to the questions below.

GetAllUniqueUsers():

This function finds all the unique users in the database.

GetMostLinkingUsers():

Get Most Linking Users:
```
{u'mentions': 549, u'_id': u'lost_dog'}
{u'mentions': 310, u'_id': u'tweetpet'}
{u'mentions': 251, u'_id': u'VioletsCRUK'}
{u'mentions': 246, u'_id': u'what_bugs_u'}
{u'mentions': 245, u'_id': u'tsarnick'}
```

This function prints the top 10 most others mentioning/linking users.

GetMostLinkedUsers():

Get Most Linked Users:
```
{u'total': 4310, u'_id': u'@mileycyrus'}
{u'total': 3837, u'_id': u'@tommcfly'}
{u'total': 3349, u'_id': u'@ddlovato'}
{u'total': 1263, u'_id': u'@Jonasbrothers'}
{u'total': 1222, u'_id': u'@DavidArchie'}
```


This function prints the top 5 most mentioned/linked users.

GetMostActiveUser():

Get Most Active Users:
```
{u'total': 549, u'_id': u'lost_dog'}
{u'total': 345, u'_id': u'webwoke'}
{u'total': 310, u'_id': u'tweetpet'}
{u'total': 281, u'_id': u'SallytheShizzle'}
{u'total': 279, u'_id': u'VioletsCRUK'}
{u'total': 276, u'_id': u'mcraddictal'}
{u'total': 248, u'_id': u'tsarnick'}
{u'total': 246, u'_id': u'what_bugs_u'}
{u'total': 238, u'_id': u'Karen230683'}
{u'total': 236, u'_id': u'DarkPiano'}
```


This function finds the top 10 most actice users that posted the most tweets.

GetMostNegativeTweets():

This function returns top 5 most negative users. That used specific keywords indicated in the function (ex. sad, pissed, mad, etc.), polarity and the amount of negative tweets.

GetMostPositiveTweets():

This function returns top 5 most positive users. That used specific keywords indicated in the function (ex. happy, amazing, excited, etc.), polarity and the amount of positive tweets.

Queries corresponding to the following questions:

    How many Twitter users are in the database?
    Which Twitter users link the most to other Twitter users? (top ten.)
    Who are the most mentioned Twitter users? (top five.)
    Who are the most active Twitter users? (top ten)
    Who are the five most negative tweets and the most positive tweets? (five users for each group)
