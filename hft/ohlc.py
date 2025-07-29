import pandas as pd
from datetime import datetime, timedelta

def trades_to_ohlcv(csv_file, frequency='1T', symbol_filter=None):
    """
    Convert trade data to OHLCV format

    Parameters:
    csv_file: path to CSV file
    frequency: pandas frequency string ('1T' for 1min, '5T' for 5min, '1S' for 1sec, etc.)
    symbol_filter: specific symbol to filter (None for all symbols)

    Returns:
    DataFrame with OHLCV data
    """
    # Read CSV
    df = pd.read_csv(csv_file, on_bad_lines='skip', low_memory=False)


    # Filter by symbol if specified
    if symbol_filter:
        df = df[df['Symbol'] == symbol_filter]

    # Set datetime as index
    df.set_index('Trade Time', inplace=True)

    # Group by symbol and frequency, then aggregate
    ohlcv = df.groupby(pd.Grouper(freq=frequency)).agg({
        'Trade Price': ['first', 'max', 'min', 'last'],  # OHLC
        'Trade Quantity': 'sum',  # Volume
        'Trade Number': 'count'   # Number of trades
    }).round(2)

    # Flatten column names
    ohlcv.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Trades']

    # Fill missing periods: Volume=0, Trades=0, Prices=previous close
    ohlcv['Volume'] = ohlcv['Volume'].fillna(0)
    ohlcv['Trades'] = ohlcv['Trades'].fillna(0)
    ohlcv[['Open', 'High', 'Low', 'Close']] = ohlcv[['Open', 'High', 'Low', 'Close']].fillna(method='ffill')

    # Or remove periods with no trades
    # ohlcv = ohlcv.dropna()

    return ohlcv

# Usage examples:
# For 1-minute OHLCV for all symbols
ohlcv_1min = trades_to_ohlcv('data/trades_1.csv', '1T')

# For 5-second OHLCV for specific symbol
# ohlcv_5sec = trades_to_ohlcv('data/trades_1.csv', '5S')

# For 1-second OHLCV
# ohlcv_1sec = trades_to_ohlcv('data/trades_1.csv', '1S')

# Print sample output
print(ohlcv_1min.head())

