import os
import pandas as pd
import requests


class AlphaVantageProvider:
    def __init__(self):
        self.api_key = os.environ['ALPHA_VANTAGE_API_KEY']
        self.endpoint = 'https://www.alphavantage.co/query'
        self.headers = {'Content-Type': 'application/json'}

    def get_historical_data(self, symbol: str, days: int) -> pd.DataFrame:
        params = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': symbol,
            'outputsize': 'compact',
            'apikey': self.api_key,
        }
        response = requests.get(self.endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        df.columns = [f'{col.split(".")[0]}_{col.split(".")[1]}' for col in df.columns]
        return df[-days:]

