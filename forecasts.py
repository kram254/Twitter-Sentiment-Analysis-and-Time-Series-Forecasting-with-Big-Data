import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import numpy as np

# Read the dataset and create a DataFrame
df = pd.read_csv('CleanedProjectTweets.csv', header=None)
df.columns = ['index', 'timestamp', 'date', 'query', 'username', 'tweet']

# Create a 'y' column; for demonstration, I'm using the length of each tweet
df['y'] = df['tweet'].str.len()

# Check the shape of the DataFrame for debugging
print(f"The shape of the DataFrame is: {df.shape}")

# Separate the processing of ARIMA and Random Forest based on DataFrame size

# ARIMA model
if 0 < len(df) < 1e6:  # You can change 1e6 to a reasonable upper limit for ARIMA
    df_sample = df.sample(frac=0.1)
    model_arima = ARIMA(df_sample['y'], order=(5, 1, 0))
    model_fit_arima = model_arima.fit()
    forecast_arima_week = model_fit_arima.forecast(steps=7)
    forecast_arima_month = model_fit_arima.forecast(steps=30)
    forecast_arima_3months = model_fit_arima.forecast(steps=90)

# Random Forest model
if len(df) > 0:
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df['y']
    model_rf = RandomForestRegressor(n_estimators=100)
    model_rf.fit(X, y)
    future_week = np.array(range(len(df), len(df) + 7)).reshape(-1, 1)
    future_month = np.array(range(len(df), len(df) + 30)).reshape(-1, 1)
    future_3months = np.array(range(len(df), len(df) + 90)).reshape(-1, 1)
    forecast_rf_week = model_rf.predict(future_week)
    forecast_rf_month = model_rf.predict(future_month)
    forecast_rf_3months = model_rf.predict(future_3months)
else:
    print("The DataFrame is empty.")

# Plotting the Forecasts
plt.figure(figsize=(12, 6))

# ARIMA Plots
if 'forecast_arima_week' in locals():
    plt.subplot(1, 2, 1)
    plt.title('ARIMA Forecast')
    plt.plot(forecast_arima_3months, label='3 Months')
    plt.plot(forecast_arima_month, label='1 Month')
    plt.plot(forecast_arima_week, label='1 Week')
    plt.legend()

# Random Forest Plots
if 'forecast_rf_week' in locals():
    plt.subplot(1, 2, 2)
    plt.title('Random Forest Forecast')
    plt.plot(forecast_rf_3months, label='3 Months')
    plt.plot(forecast_rf_month, label='1 Month')
    plt.plot(forecast_rf_week, label='1 Week')
    plt.legend()

plt.show()
