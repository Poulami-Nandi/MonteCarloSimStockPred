import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import yfinance as yf
from datetime import datetime, timedelta

# Execute Monte Carlo simulation using Monte_Carlo_Sim class for NASDAQ Quantum Computing stocks
nasdaq_quantum_computing_stocks = [
    'IBM',   # International Business Machines Corporation (IBM Quantum)
    'GOOG',  # Alphabet Inc. (Google Quantum AI)
    'MSFT',  # Microsoft Corporation (Microsoft Quantum)
    'AMZN',  # Amazon.com, Inc. (Amazon Braket - Quantum computing service)
    'AAPL',  # Apple Inc. (investing in quantum computing research)
    'INTC',  # Intel Corporation (Intel's Quantum Computing efforts)
    'RIVN',  # Rivian Automotive, Inc. (although primarily an EV company, has investments in quantum computing)
    'QLC',   # Quantum Computing Inc. (company focused on quantum computing technologies)
    'QUBT',  # Quantum Computing, Inc. (QUBT - focused on quantum computing solutions)
    'DODU',  # Dodo (company involved in quantum cryptography and security solutions)
    'ARQQ',  # ArQule, Inc. (investing in quantum tech for drug discovery and material science)
    'CASI',  # CASI Pharmaceuticals, Inc. (involved in research with quantum computing technologies)
    'NVAX',  # Novavax, Inc. (has invested in quantum computing for biotech and drug research)
]

# Get today's date
today = datetime.now().strftime('%Y-%m-%d')
# Convert today's date to a pandas datetime object
today_date = pd.to_datetime(today)
# Get the previous business day
previous_business_day = today_date - pd.offsets.BDay(1)
# Format the previous business day as a string
previous_business_day_str = previous_business_day.strftime('%Y-%m-%d')

end_date = previous_business_day_str  # previous businesss date in YYYY-MM-DD format
start_date = (previous_business_day - timedelta(days=4*365)).strftime('%Y-%m-%d')  # 4 years before the last business day


# dict to jhold results
results = {}

# Loop through each ticker and run the simulation
for ticker in nasdaq_quantum_computing_stocks:
    simulation = Monte_Carlo_Sim(ticker, start_date, end_date, 10, 5000)
    simulation.calculate_percentile_price_for_days()
    simulation.simulation_plot()
    simulation.plot_CI_price()
    simulation.plot_stock_data_column('Close')
    simulation.plot_stock_data_column('Volume')
