import pandas as pd

# Loading the dataset
data = pd.read_csv("ProjectTweets.csv")

print(data.head())

# Handle Missing Values
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

# Handling Duplicates
data.drop_duplicates(inplace=True)

# Save the Cleaned Dataset

data.to_csv("CleanedProjectTweets.csv", index=False)

# display summary statistics or other exploratory data analysis
print(data.describe())
