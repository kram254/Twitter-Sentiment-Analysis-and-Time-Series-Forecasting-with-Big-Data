import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import mean_squared_error

# Initialize the Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment
def calculate_sentiment(tweet):
    sentiment_score = sia.polarity_scores(tweet)['compound']
    return sentiment_score

# Read the CSV file
try:
    df = pd.read_csv('CleanedProjectTweets.csv', header=None)
    if df.empty:
        print("The DataFrame is empty. Exiting the program.")
        exit()
except FileNotFoundError:
    print("CSV file not found. Please make sure the file is in the correct directory.")
    exit()

# Assuming the tweet text is in the 5th column (index 4)
tweet_column_index = 4

try:
    # Calculate sentiment scores
    df['sentiment'] = df.iloc[:, tweet_column_index].apply(calculate_sentiment)
except IndexError:
    print("Index out of bounds. Please make sure you have provided the correct tweet_column_index.")
    exit()

# Calculate mean squared error (dummy example, replace y_true with actual values)
y_true = [0.5]*len(df['sentiment'])  # Replace this with actual values if you have them
y_pred = df['sentiment'].to_list()

mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error:", mse)

# Save to a new CSV if needed
df.to_csv('AnalyzedTweets.csv', index=False)
