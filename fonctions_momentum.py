#All the functions used in the momentum strategy are defined here.
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_check(stock):
    """
    Check the data of the chosen stock. If the data is not available, it will return an error message.

    Parameters:
    stock : str
        The ticker symbol of the stock to check.
    Returns:
    pd.DataFrame
        The historical data of the stock.
    """
    return yf.download(stock, start="2020-01-01", interval="1d", auto_adjust=False)

def extract_close_prices(history_data):
    """
    Extract the close prices from the historical data.

    Parameters:
    history_data : pd.DataFrame
        The historical data of the stock.
    Returns:
    pd.Series
        The close prices of the stock.
    """
    if isinstance(history_data.columns, pd.MultiIndex):
        close = history_data.xs('Close', level=0, axis=1)
    else:
        close = history_data['Close']

    return close.dropna()

def extract_volume(history_data):
    """
    Extract the volume data from the historical data.

    Parameters:
    history_data : pd.DataFrame
        The historical data of the stock.
    Returns:
    pd.Series
        The volume data of the stock.
    """
    if isinstance(history_data.columns, pd.MultiIndex):
        volume = history_data.xs('Volume', level=0, axis=1)
    else:
        volume = history_data['Volume']

    return volume.dropna()