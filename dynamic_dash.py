# Import required libraries
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Create a Dash application
app = dash.Dash(__name__)

# Read the dataset from the CSV file
df = pd.read_csv('sentiment_analysis_results.csv')

# Give proper column names based on your sample data
df.columns = ['row_id', 'id', 'timestamp', 'query', 'user', 'text', 'sentiment']

# Convert the timestamp column to datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Count the sentiments and reset the index
df_count = df.groupby([pd.Grouper(key='timestamp', freq='H'), 'sentiment']).size().reset_index(name='count')

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Tweet Sentiments Over Time"),

    dcc.Dropdown(
        id='sentiment-dropdown',
        options=[
            {'label': 'Positive', 'value': 'positive'},
            {'label': 'Negative', 'value': 'negative'},
            {'label': 'Neutral', 'value': 'neutral'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # Default value
        multi=False
    ),

    dcc.Graph(id='line-plot'),
])

# Callback to update the line plot based on dropdown selection
@app.callback(
    Output('line-plot', 'figure'),
    [Input('sentiment-dropdown', 'value')]
)
def update_graph(selected_sentiment):
    if selected_sentiment == 'all':
        fig = px.line(df_count, x='timestamp', y='count', color='sentiment', title='All Sentiments Over Time')
    else:
        filtered_df = df_count[df_count['sentiment'] == selected_sentiment]
        fig = px.line(filtered_df, x='timestamp', y='count', title=f'{selected_sentiment.capitalize()} Sentiments Over Time')

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)



