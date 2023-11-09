# Sentiment Analysis and Time Series Forecasting Project
## Overview
This project is aimed at performing sentiment analysis on Twitter data and forecasting sentiment trends over time. The project uses Apache Spark for data processing, the MongoDB Spark connector for data storage, and the SARIMAX model for time series forecasting.

## Requirements
Apache Spark 3.5.0
Python 3.8 or higher
MongoDB 4.4 or higher
Pyspark
Statsmodels (for SARIMAX)
Pandas

## Installation and Setup
### Apache Spark Setup
Ensure that Apache Spark 3.5.0 is installed on your system. If not, download and install it from the official website.

### MongoDB Setup
Install MongoDB from the official website and ensure it is running on its default port (27017).

### Python Dependencies
Install the required Python libraries using pip:
```
pip install pyspark pandas statsmodels
MongoDB Spark Connector
```

Include the MongoDB Spark Connector dependency in your SparkSession builder:

```
.config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1")
```
Make sure that the version of the MongoDB connector is compatible with Spark 3.5.0.

### Project Structure
```
SentimentTimeSeries/
|-- data/
|   `-- <INSERT_DATA_FILES_HERE>
|-- notebooks/
|   `-- analysis.ipynb
|-- src/
|   |-- __init__.py
|   |-- sentiment_analysis.py
|   `-- time_series_forecasting.py
`-- README.md
```

**data/:** Directory containing the datasets.
**notebooks/:** Jupyter notebooks for exploratory data analysis.
**src/:** Python modules for sentiment analysis and time series forecasting.
**README.md:** This README file.

### Usage
## Data Ingestion
**Start your MongoDB instance**
Ingest the Twitter data into MongoDB using the appropriate import commands.

### Sentiment Analysis
To run the sentiment analysis:
```
from src.sentiment_analysis import sentiment_analysis
```
sentiment_analysis()
This will process the Twitter data, perform sentiment analysis, and store the results back into MongoDB.

### Time Series Forecasting
To execute the time series forecasting:
```
from src.time_series_forecasting import run_time_series_forecasting
```
run_time_series_forecasting()
This will retrieve the sentiment data from MongoDB, apply the SARIMAX model, and save the forecasts into MongoDB.

#### Running the Notebooks
To explore the data and models, launch the Jupyter notebook:
``` 
jupyter notebook notebooks/analysis.ipynb
```
## Configuration
Configuration parameters for MongoDB and Spark can be set in the src/config.py file:


```
MONGO_URI = "<INSERT_MONGO_CONNECTION_URI>"
DATABASE_NAME = "<INSERT_DATABASE_NAME>"
COLLECTION_NAME = "<INSERT_COLLECTION_NAME>"
```

### Deployment
Instructions for deploying the application in a production environment.

### Contributing
Details on how others can contribute to the project.

### License
GNU

### Contact
Information on how to reach out to the maintainers of the project.
**markorlando45@gmail.com**