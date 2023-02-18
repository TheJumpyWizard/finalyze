import requests
import pandas as pd


def fetch_historical_data(api_key: str, symbol: str, days: int) -> pd.DataFrame:
    # Construct the API endpoint URL
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize={days}&apikey={api_key}'

    # Fetch the data from the API
    response = requests.get(url)
    data = response.json()

    # Convert the response to a DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    return df

