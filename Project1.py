import os
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

from credentials import *    # This will allow us to use the keys as variables
import tweepy #import here to make the program happy
import networkx as nx
import Graphs

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Return API with authentication:
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

# We create an extractor object:
extractor = twitter_setup()

user = "jeong5020"                                                        
user_ids = [967356154119516161]

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name=user, count=200)
user_objects = extractor.lookup_users(screen_names=user)
user_ids = [user.id_str for user in user_objects]
print(user_ids)
'''
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
data['ID']   = [tweet.id for tweet in tweets]
#data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])

g = Graphs.Graphs(user_ids[0])
g.construct(data['ID'][:5])
g.measurements()
#g.graph_visualize()
#g.degree_histogram()

tweets = extractor.mentions_timeline(screen_name=user, count=200)                   
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
                                                                               
g = Graphs.Graphs(user_ids[0])                                                  
g.construct(data['ID'][:5])                                                     
g.measurements()                                                                
#g.graph_visualize()                                                            
#g.degree_histogram()
'''
name = 'LunarCRUSH'
tweet_id = '1270923526690664448'
edges=[]
for tweet in tweepy.Cursor(extractor.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
    #if hasattr(tweet, 'in_reply_to_status_id_str'):
    #    if (tweet.in_reply_to_status_id_str==tweet_id):
    row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
    edges.append(row['user'])    
g = Graphs.Graphs(name)#user_ids[0])                                                  
g.construct(edges[:10])                                                     
g.measurements()                                                                
#g.graph_visualize()                                                            
g.degree_histogram() 
