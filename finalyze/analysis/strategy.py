import pandas as pd


def generate_trading_signal(data: pd.DataFrame, sma_20: pd.Series, sma_50: pd.Series, rsi: pd.Series) -> pd.Series:
    # Generate trading signals based on technical analysis
    signal = pd.Series(index=data.index)
    signal[sma_20 > sma_50] = 1  # buy signal
    signal[sma_20 < sma_50] = -1  # sell signal
    signal[rsi > 70] = -1  # sell signal
    signal[rsi < 30] = 1  # buy signal

    # Set any remaining signals to hold
    signal.fillna(0, inplace=True)

    return signal

