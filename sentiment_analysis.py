import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pymongo import MongoClient
from sklearn.metrics import mean_squared_error  # Ensure you've installed scikit-learn

# Downloading the VADER sentiment analysis lexicon
nltk.download("vader_lexicon")

# Initializing the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Connecting to MongoDB and retrieving data
# Modify the MongoDB connection string as needed
client = MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client.projecttweetsdb
collection = db.tweets

# Querying MongoDB to retrieve the data (modify the query as needed)
cursor = collection.find({})

# Print the retrieved data for debugging
print("Retrieved data from MongoDB:")
print(list(cursor))

# Creating an empty DataFrame to store the data
df = pd.DataFrame(list(cursor))

# Check if the DataFrame is empty and exit if true
if df.empty:
    print("The DataFrame is empty. Exiting the program.")
    exit()

# Define a function to calculate sentiment scores
def calculate_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    sentiment = ""
    if sentiment_scores["compound"] >= 0.05:
        sentiment = "positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment

# Assuming the tweet text is in the first column of the DataFrame
# Modify the column index accordingly if needed (0 is the first column)
tweet_column_index = 6  

# Apply sentiment analysis to the tweet text column
df["sentiment"] = df.iloc[:, tweet_column_index].apply(calculate_sentiment)

# Export the DataFrame to a CSV file
df.to_csv("sentiment_analysis_results.csv", index=False)

# Implement the remaining tasks as mentioned in your requirements.







# import pandas as pd
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from pymongo import MongoClient 

# # Downloading the VADER sentiment analysis lexicon 
# nltk.download("vader_lexicon")

# # Initializing the sentiment analyzer
# sia = SentimentIntensityAnalyzer()

# # Connecting to MongoDB and retrieve data
# # Modifying the MongoDB connection string as needed
# client = MongoClient("mongodb://localhost:27017")

# # Selecting the database and collection
# db = client.projecttweetsdb
# collection = db.tweets

# # Querying MongoDB to retrieve the data (modify the query as needed)
# cursor = collection.find({})

# # Creating an empty DataFrame to store the data
# df = pd.DataFrame(list(cursor))

# # Define a function to calculate sentiment scores
# def calculate_sentiment(text):
#    sentiment_scores = sia.polarity_scores(text)
#    sentiment = ""
#    if sentiment_scores["compound"] >= 0.05:
#        sentiment = "positive"
#    elif sentiment_scores["compound"] <= -0.05:
#        sentiment = "negative"
#    else:
#        sentiment = "neutral"
#    return sentiment

# # Assuming the tweet text is in the fourth column (index 3)
# # Modify the index accordingly if needed
# df["sentiment"] = df.iloc[:, 3].apply(calculate_sentiment)

# # Export the DataFrame to a CSV file
# df.to_csv("sentiment_analysis_results.csv", index=False)
