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

This function prints the top 10 most others mentioning/linking users.

GetMostLinkedUsers():

This function prints the top 5 most mentioned/linked users.

GetMostActiveUser():

This function finds the top 5 most actice users that posted the most tweets.

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
