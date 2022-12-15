import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Set up the Twitter API client
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Set up the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Search for tweets containing the specified keyword or hashtag
tweets = api.search(q="keyword or hashtag")

# Analyze the sentiment of each tweet
sentiments = []
for tweet in tweets:
  text = tweet.text
  sentiment = sid.polarity_scores(text)
  sentiments.append(sentiment)
  
# Aggregate the results and display an overall sentiment score
positive_sentiments = [s for s in sentiments if s > 0]
neutral_sentiments = [s for s in sentiments if s == 0]
negative_sentiments = [s for s in sentiments if s < 0]

total = len(sentiments)
pos_percent = len(positive_sentiments) / total
neu_percent = len(neutral_sentiments) / total
neg_percent = len(negative_sentiments) / total

print("Overall sentiment score:")
print("Positive: %.2f%%" % (pos_percent * 100))
print("Neutral: %.2f%%" % (neu_percent * 100))
print("Negative: %.2f%%" % (neg_percent * 100))
