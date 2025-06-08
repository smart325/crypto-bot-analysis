import pandas as pd
import ta

def compute_indicators(df):
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['ma50'] = df['close'].rolling(window=50).mean()
    df['ma200'] = df['close'].rolling(window=200).mean()
    return df
