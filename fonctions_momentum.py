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
    return yf.download(stock, start="2020-01-01", interval="1d", auto_adjust=True)

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

def plot_close_prices(close_prices, stock):
    """
    Plot the close prices of the stock.

    Parameters:
    close_prices : pd.Series
        The close prices of the stock.
    stock : str
        The ticker symbol of the stock.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(close_prices.index, close_prices.values)
    plt.title(f'Close Prices of {stock}')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid()
    plt.show()

def plot_volume(volume_data, stock):
    """
    Plot the volume data of the stock.

    Parameters:
    volume_data : pd.Series
        The volume data of the stock.
    stock : str
        The ticker symbol of the stock.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(volume_data.index, volume_data.values)
    plt.title(f'Volume Data of {stock}')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid()
    plt.show()

def dollar_cost_average_investment(close_prices, investment_amount, investment_frequency):
    """
    Calculate the dollar-cost average investment strategy.

    Parameters:
    close_prices : pd.Series
        The close prices of the stock.
    investment_amount : float
        The amount to invest at each interval.
    investment_frequency : str
        The frequency of investment (e.g., '1M' for monthly, '1W' for weekly).
    Returns:
    pd.DataFrame
        A DataFrame containing the total shares purchased and total invested amount over time.
    """
    if isinstance(close_prices, pd.DataFrame):
        if close_prices.shape[1] != 1:
            raise ValueError("close_prices must contain only one stock.")

        close_prices = close_prices.iloc[:, 0]
    # Resample the close prices based on the investment frequency
    resampled_prices = close_prices.resample(investment_frequency).last().dropna()
    
    # Calculate the number of shares purchased at each interval
    shares_purchased = investment_amount / resampled_prices
    
    # Calculate cumulative shares, total invested amount, portfolio value, and investment % gain
    cumulative_shares = shares_purchased.cumsum()

    total_invested = np.arange(1, len(cumulative_shares) + 1) * investment_amount

    portfolio_value = cumulative_shares * resampled_prices

    pct_gain = ((cumulative_shares * resampled_prices) / total_invested - 1) * 100
    
    return pd.DataFrame({
        'Total Shares': cumulative_shares,
        'Total Invested': total_invested,
        'Portfolio Value': portfolio_value,
        'Percentage Gain': pct_gain
    }, index=resampled_prices.index)


def extract_tickers(file_path):
    """
    Extract the ticker symbols from a text file. In this case, this if for the S&P 500 tickers. The text file should have the ticker symbols listed one per line, with the first two lines being headers that will be skipped.

    Parameters:
    file_path : str
        The path to the text file containing the ticker symbols.
    Returns:
    list
        A list of ticker symbols.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Skip the header line
        next(file)  # Skip the second line

        tickers = [line.strip() for line in file if line.strip()]
    return tickers