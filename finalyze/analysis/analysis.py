import pandas as pd
from typing import Tuple
from .indicators import calculate_moving_averages, calculate_rsi
from .strategy import generate_trading_signal


def analyze_data(data: pd.DataFrame, symbol: str) -> Tuple[pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    # Calculate technical indicators
    sma_20 = calculate_moving_averages(data, 20)
    sma_50 = calculate_moving_averages(data, 50)
    rsi = calculate_rsi(data, 14)

    return data, sma_20, sma_50, rsi


def generate_analysis_report(data: pd.DataFrame, sma_20: pd.Series, sma_50: pd.Series, rsi: pd.Series, symbol: str) -> None:
    # Generate trading signals based on the analysis
    signal = generate_trading_signal(data, sma_20, sma_50, rsi)
    print(signal)

    # Export the data and analysis to a CSV file
    output_filename = f'{symbol}_analysis.csv'
    data['20-day SMA'] = sma_20
    data['50-day SMA'] = sma_50
    data['RSI'] = rsi
    data.to_csv(output_filename, index_label='Date')

    print(f'Data and analysis saved to {output_filename}.')

