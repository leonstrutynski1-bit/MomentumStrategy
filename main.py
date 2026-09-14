import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import fonctions_momentum as fm

# The main code of my momentum strategy will be implemented in this file. It will use the functions defined in fonctions_momentum.py to perform the necessary calculations and generate the desired outputs.

chosen_stock = input("Enter the ticker symbol of the stock you want to analyze: ")
# Check the data of the chosen stock
history_data = fm.data_check(chosen_stock)
print(history_data.head())
print(history_data.tail())
close_prices = fm.extract_close_prices(history_data)
print(close_prices.head())
volume_data = fm.extract_volume(history_data)
print(volume_data.head())
