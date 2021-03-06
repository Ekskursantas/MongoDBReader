Follow the steps to get the database and MongoDB:


Firstly, install Docker:

````wget -O - https://bit.ly/docker-install | bash````

After Docker is installed you need to setup your MongoDB:

```sudo docker run --rm -v $(pwd)/data:/data/db --name dbms --publish=27017:27017 -d mongo:latest```

```docker exec -it dbms bash```
or 
```docker exec -it 98ac bash``` 

You can get the for digits from ```docker ps``` and take the first 4 digits from the container id.

The you will directed to the dockers bash where you will need to download wget and unzip:

```apt-get update```
```apt-get install -y wget```
```apt-get install -y unzip```

Then you will need to download the data you will store in the database:

```wget http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip```

Unzip it:

```unzip trainingandtestdata.zip```

We create the headerlines (fields) for the data from the CSV:

```sed -i '1s;^;polarity,id,date,query,user,text\n;' training.1600000.processed.noemoticon.csv```

Finally we import the data to MongoDB:

```mongoimport --drop --db social_net --collection tweets --type csv --headerline --file training.1600000.processed.noemoticon.csv```

After MongoDB container is setup, we finally can use our python script via terminal. We locate ourself to the folder where the script is located and the run the syntax:

```python MongoDBReader.py```

It will print out all the answers to the questions below.

GetAllUniqueUsers():

Get Total Number Of Unique Users
```
659774
```

This function finds all the unique users in the database.

GetMostLinkingUsers():

Get Most Linking Users:
```
{u'mentions': 549, u'_id': u'lost_dog'}
{u'mentions': 310, u'_id': u'tweetpet'}
{u'mentions': 251, u'_id': u'VioletsCRUK'}
{u'mentions': 246, u'_id': u'what_bugs_u'}
{u'mentions': 245, u'_id': u'tsarnick'}
{u'mentions': 229, u'_id': u'SallytheShizzle'}
{u'mentions': 217, u'_id': u'mcraddictal'}
{u'mentions': 216, u'_id': u'Karen230683'}
{u'mentions': 211, u'_id': u'keza34'}
{u'mentions': 202, u'_id': u'TraceyHewins'}

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

Get The Saddest Users:
```
{u'emotion': 0.0, u'_id': u'PaoloAlonso', u'total_negative_tweets': 20}
{u'emotion': 0.0, u'_id': u'yanarropak', u'total_negative_tweets': 12}
{u'emotion': 0.0, u'_id': u'x0xnina', u'total_negative_tweets': 8}
{u'emotion': 0.0, u'_id': u'Arantza92', u'total_negative_tweets': 8}
{u'emotion': 0.0, u'_id': u'sbjayy', u'total_negative_tweets': 8}
```

This function returns top 5 most negative users. That used specific keywords indicated in the function (ex. sad, pissed, mad, etc.), polarity and the amount of negative tweets.

GetMostPositiveTweets():

Get The Happiest Users:
```
{u'emotion': 4.0, u'_id': u'caldjr', u'total_positive_tweets': 40}
{u'emotion': 4.0, u'_id': u'jessa_hugz', u'total_positive_tweets': 29}
{u'emotion': 4.0, u'_id': u'DarkPiano', u'total_positive_tweets': 29}
{u'emotion': 4.0, u'_id': u'josephranseth', u'total_positive_tweets': 25}
{u'emotion': 4.0, u'_id': u'kjgriffin18', u'total_positive_tweets': 23}
```
This function returns top 5 most positive users. That used specific keywords indicated in the function (ex. happy, amazing, excited, etc.), polarity and the amount of positive tweets.

Queries corresponding to the following questions:

    How many Twitter users are in the database?
    Which Twitter users link the most to other Twitter users? (top ten.)
    Who are the most mentioned Twitter users? (top five.)
    Who are the most active Twitter users? (top ten)
    Who are the five most negative tweets and the most positive tweets? (five users for each group)
