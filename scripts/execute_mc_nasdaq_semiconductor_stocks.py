import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import yfinance as yf
from datetime import datetime, timedelta

# Execute Monte Carlo simulation using Monte_Carlo_Sim class for NASDAQ Semiconductor stocks
nasdaq_semiconductor_stocks = [
    'NVDA',  # NVIDIA Corporation
    'INTC',  # Intel Corporation
    'AMD',   # Advanced Micro Devices, Inc.
    'MU',    # Micron Technology, Inc.
    'TXN',   # Texas Instruments Incorporated
    'SWKS',  # Skyworks Solutions, Inc.
    'QCOM',  # Qualcomm Incorporated
    'AMAT',  # Applied Materials, Inc.
    'LSCC',  # Lattice Semiconductor Corporation
    'MRVL',  # Marvell Technology Group Ltd.
    'ON',    # ON Semiconductor Corporation
    'AVGO',  # Broadcom Inc.
    'ASML',  # ASML Holding NV (based in the Netherlands, but listed on NASDAQ)
    'KLAC',  # KLA Corporation
    'IDTI',  # Integrated Device Technology, Inc. (now part of Renesas)
    'CRUS',  # Cirrus Logic, Inc.
    'STX',   # Seagate Technology Holdings PLC (though primarily a storage company, they are in the semiconductor field)
    'SIMG',  # Silicon Motion Technology Corporation
    'IPHI'   # Inphi Corporation (now part of Marvell Technology)
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
for ticker in nasdaq_semiconductor_stocks:
    simulation = Monte_Carlo_Sim(ticker, start_date, end_date, 10, 5000)
    simulation.calculate_percentile_price_for_days()
    simulation.simulation_plot()
    simulation.plot_CI_price()
    simulation.plot_stock_data_column('Close')
    simulation.plot_stock_data_column('Volume')
