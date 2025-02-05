import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import yfinance as yf
from datetime import datetime, timedelta

# Execute Monte Carlo simulation using Monte_Carlo_Sim class for NASDAQ AI stocks
nasdaq_ai_stocks = [
    'GOOG',  # Alphabet (Google)
    'GOOGL', # Alphabet (Google)
    'NVDA',  # NVIDIA Corporation
    'MSFT',  # Microsoft Corporation
    'AMZN',  # Amazon.com, Inc.
    'AAPL',  # Apple Inc.
    'INTC',  # Intel Corporation
    'META',  # Meta Platforms, Inc. (formerly Facebook)
    'AMD',   # Advanced Micro Devices, Inc.
    'BA',    # Boeing (AI applications in manufacturing)
    'TSLA',  # Tesla, Inc. (AI in autonomous driving)
    'ORCL',  # Oracle Corporation
    'CRM',   # Salesforce.com, Inc. (AI for CRM tools)
    'IBM',   # International Business Machines Corporation
    'ZS',    # Zscaler, Inc. (AI in cybersecurity)
    'PYPL',  # PayPal Holdings, Inc. (AI in payment processing)
    'MU',    # Micron Technology, Inc. (AI in memory products)
    'ADBE',  # Adobe Inc. (AI in creative and marketing solutions)
    'INTU',  # Intuit Inc. (AI for personal finance and accounting)
    'NOW'    # ServiceNow, Inc. (AI in workflow automation)
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
for ticker in nasdaq_ai_stocks:
    simulation = Monte_Carlo_Sim(ticker, start_date, end_date, 10, 5000)
    simulation.calculate_percentile_price_for_days()
    simulation.simulation_plot()
    simulation.plot_CI_price()
    simulation.plot_stock_data_column('Close')
    simulation.plot_stock_data_column('Volume')
