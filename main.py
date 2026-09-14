import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import fonctions_momentum as fm

# The main code of my momentum strategy will be implemented in this file. It will use the functions defined in fonctions_momentum.py to perform the necessary calculations and generate the desired outputs.


chosen_stock = input("Enter the ticker symbol of the stock you want to analyze: ")

passive_strategy = fm.data_check('VOO')
passive_closing_prices = fm.extract_close_prices(passive_strategy)
print(passive_strategy.head())
print(passive_strategy.tail())
dollar_investment = fm.dollar_cost_average_investment(passive_closing_prices, 200, '1M')
print(dollar_investment.tail())

# Check the data of the chosen stock
history_data = fm.data_check(chosen_stock)
print(history_data.head())
print(history_data.tail())
close_prices = fm.extract_close_prices(history_data)
print(close_prices.head())
volume_data = fm.extract_volume(history_data)
print(volume_data.head())

plot_choice = input("Do you want to plot the close prices and volume? (yes/no): ")
if plot_choice.lower() == 'yes':
    fm.plot_close_prices(close_prices, chosen_stock)
    fm.plot_volume(volume_data, chosen_stock)
