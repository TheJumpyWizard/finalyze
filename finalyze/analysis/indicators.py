import pandas as pd


def calculate_moving_averages(data: pd.DataFrame, window: int) -> pd.Series:
    # Calculate the simple moving average of the close price
    return data['Close'].rolling(window=window).mean()


def calculate_rsi(data: pd.DataFrame, window: int) -> pd.Series:
    # Calculate the relative strength index (RSI) using the close price
    delta = data['Close'].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    average_gain = gain.rolling(window=window).mean()
    average_loss = loss.rolling(window=window).mean()

    relative_strength = average_gain / average_loss
    rsi = 100 - (100 / (1 + relative_strength))

    return rsi

