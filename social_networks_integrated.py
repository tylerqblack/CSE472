import tweepy
import pandas as pd
import numpy as np
import json # The API returns JSON formatted text
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import collections
#from credentials import *

access_token = "xxx"                                                            
access_token_secret = "xxx"                                                     
consumer_key = "xxx"                                                            
consumer_secret = "xxx" 

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

TRACKING_KEYWORDS = ['Covid']
OUTPUT_FILE = "Covid_tweets.txt"
TWEETS_TO_CAPTURE = 3000

class MyStreamListener(tweepy.StreamListener):
    """
    Twitter listener, collects streaming tweets and output to a file
    """
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open(OUTPUT_FILE, "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        
        # Stops streaming when it reaches the limit
        if self.num_tweets <= TWEETS_TO_CAPTURE:
            if self.num_tweets % 100 == 0: # just to see some progress...
                print('Numer of tweets captured so far: {}'.format(self.num_tweets))
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

#%%time #let's see how long it takes

# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=TRACKING_KEYWORDS)

# Initialize empty list to store tweets
tweets_data = []

# Open connection to file
with open(OUTPUT_FILE, "r") as tweets_file:
    # Read in tweets and store in list
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_data.append(tweet)

pd.set_option('display.float_format', lambda x: '%.f' % x)
tweets_df = pd.read_json("Covid_tweets.txt", lines=True)

tweets_final = pd.DataFrame(columns = ["created_at", "id", "in_reply_to_screen_name", "in_reply_to_status_id", "in_reply_to_user_id",
                                      "retweeted_id", "retweeted_screen_name", "user_mentions_screen_name", "user_mentions_id", 
                                       "text", "user_id", "screen_name", "followers_count"])
print(tweets_final.head())
print(tweets_final.columns)

# Columns that are going to be the same
equal_columns = ["created_at", "id", "text"]
tweets_final[equal_columns] = tweets_df[equal_columns]

# Get the basic information about user 
def get_basics(tweets_final):
    tweets_final["screen_name"] = tweets_df["user"].apply(lambda x: x["screen_name"])
    tweets_final["user_id"] = tweets_df["user"].apply(lambda x: x["id"])
    tweets_final["followers_count"] = tweets_df["user"].apply(lambda x: x["followers_count"])
    return tweets_final

# Get the user mentions 
def get_usermentions(tweets_final):
    # Inside the tag 'entities' will find 'user mentions' and will get 'screen name' and 'id'
    tweets_final["user_mentions_screen_name"] = tweets_df["entities"].apply(lambda x: x["user_mentions"][0]["screen_name"] if x["user_mentions"] else np.nan)
    tweets_final["user_mentions_id"] = tweets_df["entities"].apply(lambda x: x["user_mentions"][0]["id_str"] if x["user_mentions"] else np.nan)
    return tweets_final

# Get retweets
def get_retweets(tweets_final):
    # Inside the tag 'retweeted_status' will find 'user' and will get 'screen name' and 'id'    
    tweets_final["retweeted_screen_name"] = tweets_df["retweeted_status"].apply(lambda x: x["user"]["screen_name"] if x is not np.nan else np.nan)
    tweets_final["retweeted_id"] = tweets_df["retweeted_status"].apply(lambda x: x["user"]["id_str"] if x is not np.nan else np.nan)
    return tweets_final

# Get the information about replies
def get_in_reply(tweets_final):
    # Just copy the 'in_reply' columns to the new dataframe
    tweets_final["in_reply_to_screen_name"] = tweets_df["in_reply_to_screen_name"]
    tweets_final["in_reply_to_status_id"] = tweets_df["in_reply_to_status_id"]
    tweets_final["in_reply_to_user_id"]= tweets_df["in_reply_to_user_id"]
    return tweets_final

# Lastly fill the new dataframe with the important information
def fill_df(tweets_final):
    get_basics(tweets_final)
    get_usermentions(tweets_final)
    get_retweets(tweets_final)
    get_in_reply(tweets_final)
    return tweets_final

# Get the interactions between the different users
def get_interactions(row):
    # From every row of the original dataframe
    # First we obtain the 'user_id' and 'screen_name'
    user = row["user_id"], row["screen_name"]
    # Be careful if there is no user id
    if user[0] is None:
        return (None, None), []
    
    # The interactions are going to be a set of tuples
    interactions = set()
    
    # Add all interactions 
    # First, we add the interactions corresponding to replies adding the id and screen_name
    interactions.add((row["in_reply_to_user_id"], row["in_reply_to_screen_name"]))
    # After that, we add the interactions with retweets
    interactions.add((row["retweeted_id"], row["retweeted_screen_name"]))
    # And later, the interactions with user mentions
    interactions.add((row["user_mentions_id"], row["user_mentions_screen_name"]))
    
    # Discard if user id is in interactions
    interactions.discard((row["user_id"], row["screen_name"]))
    # Discard all not existing values
    interactions.discard((None, None))
    # Return user and interactions
    return user, interactions

tweets_final = fill_df(tweets_final)
tweets_final = tweets_final.where((pd.notnull(tweets_final)), None)
print(tweets_final.head(5))

#Use Directed graph for twitter network
graph = nx.DiGraph()

for index, tweet in tweets_final.iterrows():
    user, interactions = get_interactions(tweet)
    user_id, user_name = user
    tweet_id = tweet["id"]
    #tweet_sent = tweet["sentiment"]
    for interaction in interactions:
        int_id, int_name = interaction
        graph.add_edge(user_id, int_id, tweet_id=tweet_id)
        

        graph.nodes[user_id]["name"] = user_name
        graph.nodes[int_id]["name"] = int_name

print(f"There are {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges present in the Graph")
print(f"The average clustering coefficient is {nx.average_clustering(graph)} in the graph")
print(f"The transitivity of the graph is {nx.transitivity(graph)}")

colors_central_nodes = ['orange', 'red']
central_nodes = ['393852070', '2896294831']

pos = nx.spring_layout(graph, k=0.05)
plt.figure(figsize = (20,20))
nx.draw(graph, pos=pos, node_color=range(graph.number_of_nodes()), cmap=plt.cm.PiYG, edge_color="black", linewidths=0.3, node_size=60, alpha=0.6, with_labels=False)
#nx.draw_networkx_nodes(graph, pos=pos, nodelist=central_nodes, node_size=300, node_color=colors_central_nodes)
plt.savefig('graphfinal.png')
plt.show()


# measurements : degree distribution

degree_sequence = sorted([d for n, d in graph.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)                      
deg, cnt = zip(*degreeCount.items())                                    

fig, ax = plt.subplots()                                                        
plt.bar(deg, cnt, width=0.80, color="b")                                        
                                                                                
plt.title("Degree Histogram")                                                   
plt.ylabel("Count")                                                             
plt.xlabel("Degree")                                                            
ax.set_xticks([d + 0.4 for d in deg])                                           
ax.set_xticklabels(deg)                                                         
                                                                                
# draw graph in inset                                                           
plt.axes([0.4, 0.4, 0.5, 0.5])                                                 
pos = nx.spring_layout(graph)         
plt.savefig('degree_histogram.png')
plt.axis("off")                                                                 
plt.show()


# measurements : closeness, betweeness, and clustering coefficient
Closeness = nx.closeness_centrality(graph)
Betweeness = nx.betweenness_centrality(graph)
Clustering_coefficient = nx.clustering(graph)                      
n_bins = 20

fig, axs = plt.subplots()#1, 1, sharey=True, tight_layout=True)
y = [item for key, item in Closeness.items()]
plt.title("Closeness")                                                   
plt.ylabel("Value")                                                             
plt.xlabel("Node count")                                                            
axs.hist(y,bins=n_bins, density=False, orientation='horizontal')
plt.show()


fig, axs = plt.subplots()#1, 1, sharey=True, tight_layout=True)
y = [item for key, item in Betweeness.items()]
plt.title("Betweeness")                                                   
plt.ylabel("Value")                                                             
plt.xlabel("Node count")                                                            
axs.hist(y,bins=n_bins, density=False, orientation='horizontal')
plt.show()


fig, axs = plt.subplots()
y = [item for key, item in Clustering_coefficient.items()]
plt.title("Clustering_coefficient")                                                   
plt.ylabel("Value")                                                             
plt.xlabel("Node count")                                                            
axs.hist(y,bins=n_bins, density=False, orientation='horizontal')
plt.show()
