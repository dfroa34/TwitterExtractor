# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '2841200026-gQSl3UCP3VMhFKpQWJNfXjY0WX846KL4idI2YPU'
ACCESS_SECRET = 'eFpItW0liT4gmPeTaB3wJRMkc98SmReAHXNqRtdIB92XC'
CONSUMER_KEY = 'Qpbao6aMCktKEyp67cxi36Hyl'
CONSUMER_SECRET = 'LmaqPEr0nwIhcmPcBfEvDiiuJhERifot80AafC7jJmnOq4T6w0'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
# twitter_stream = TwitterStream(auth=oauth)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#nlproc"
iterator = twitter.search.tweets(q='Paloma')
# Get a sample of the public data following through Twitter
#iterator = twitter.Twitter(auth=oauth).statuses.sample()

print iterator

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)


   # res = json.loads(tweet)
   # if 'text' in res:  # only messages contains 'text' field is a tweet
    #    print tweet['id']  # This is the tweet's id
     #   print tweet['created_at']  # when the tweet posted
      #  print tweet['text']  # content of the tweet


    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break 