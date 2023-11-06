import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Downloading the VADER sentiment analysis lexicon
nltk.download("vader_lexicon")

# Initializing the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Reading data from the CSV file
df = pd.read_csv("CleanedProjectTweets.csv", header=None)

# Check if DataFrame is empty
if df.empty:
    print("The DataFrame is empty. Exiting the program.")
    exit()

# Function to calculate sentiment scores
def calculate_sentiment(text):
    sentiment_scores = sia.polarity_scores(str(text))
    sentiment = ""
    if sentiment_scores["compound"] >= 0.05:
        sentiment = "positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment

# Assuming the tweet text is in the last column (index 5) of the DataFrame
tweet_column_index = 5

# Apply sentiment analysis to the tweet text column
df["sentiment"] = df.iloc[:, tweet_column_index].apply(calculate_sentiment)

# Export the DataFrame to a new CSV file
df.to_csv("sentiment_analysis_results.csv", index=False)
