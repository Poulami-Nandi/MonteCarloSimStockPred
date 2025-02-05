import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import yfinance as yf
from datetime import datetime, timedelta

class Monte_Carlo_Sim():
    
    def __init__(self, ticker, start_date, end_date, nr_of_days, nr_of_sim):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.nr_of_sim = nr_of_sim
        self.nr_of_days = nr_of_days
        
        self.download_stock_data()
        self.capture_daily_returns()
        self.calculate_volatility()
        self.execute_monte_carlo()
    
    def download_stock_data(self):
        self.data = pd.DataFrame()

        # Using Yahoo Finance to download stock data
        stock = yf.Ticker(self.ticker)
        self.data = stock.history(start=self.start_date, end=self.end_date)
        
        # Check if the DataFrame is empty and print info if it is.
        if self.data.empty:
            print(f"Dataframe for ticker {self.ticker} is empty. Check data availability for the given date range.")
            print(f"Start date: {self.start_date}, End date: {self.end_date}")
            return  # Stop execution if data is empty

        self.data.to_csv(f"{self.ticker}_stock_data.csv")


    def capture_daily_returns(self):

        # calculate daily returns from Close price
        self.daily_returns = np.log(1 + self.data['Close'].pct_change())
        self.daily_returns = self.daily_returns[1:]

    def calculate_volatility(self):
        self.daily_volatility = np.std(self.daily_returns)
    
    def execute_monte_carlo(self):
        # Check if self.data is empty before accessing it.
        if self.data.empty:
            print(f"Dataframe for ticker {self.ticker} is empty. Monte Carlo simulation cannot be executed.")
            return

        # Get the last days stock price
        last_price = self.data['Close'].iloc[-1]
        self.last_price = last_price
        
        # Initialize a list to store all simulation results
        all_simulations = []

        for x in range(self.nr_of_sim):
            price_series = [last_price]

            for y in range(1, self.nr_of_days):
                price = price_series[-1] * (1 + np.random.normal(0, self.daily_volatility))
                price_series.append(price)

            all_simulations.append(price_series)

        # Convert the list of simulations into a DataFrame all at once
        self.simulation_df = pd.DataFrame(all_simulations).transpose()
                
       
    def calculate_percentile_price_for_days(self):
        for i in range(0,self.nr_of_days):
            #print(f"simulation day {i} stdev: {statistics.stdev(simulation_df.iloc[i])}")
            # calulate next day from end_date
            next_business_day = pd.to_datetime(self.end_date) + pd.offsets.BDay(1 + i)
            #print(f"The next business day after {end_date} is {next_business_day.strftime('%Y-%m-%d')}")
            # Extract the prices for the next
            # Extract the prices for the next day after end_date
            next_day_price = self.simulation_df.iloc[0 + i]

            # Calculate the 95% confidence interval
            lower_bound = np.percentile(next_day_price, 2.5)
            upper_bound = np.percentile(next_day_price, 97.5)
            # Calculate the mean (expected) price
            mean_price = np.mean(next_day_price)
            # 98% CI price
            lower_bound_98 = np.percentile(next_day_price, 1)
            upper_bound_98 = np.percentile(next_day_price, 99)
            # Print the results
            print(f"{self.ticker}: The mean price {next_business_day.strftime('%Y-%m-%d')} is: {round(mean_price,2)}, The 95% CI price: ({round(lower_bound,2)}, {round(upper_bound,2)}), The 98% CI price: ({round(lower_bound_98,2)}, {round(upper_bound_98,2)})")

    def plot_CI_price(self):
        # plot 90% CI, 95% CI, 98% CI and the mean price for each day
        forecast_dates = pd.date_range(start=self.end_date, periods=self.nr_of_days + 1, freq='B')[1:]  

        # Calculate mean and confidence intervals along the correct axis (axis=1 for row-wise)
        mean_price = self.simulation_df.mean(axis=1)
        
        # Calculate confidence intervals for each day
        ci_90 = np.array([np.percentile(self.simulation_df.iloc[i], [5, 95]) for i in range(self.nr_of_days)]) 
        ci_95 = np.array([np.percentile(self.simulation_df.iloc[i], [2.5, 97.5]) for i in range(self.nr_of_days)])
        ci_98 = np.array([np.percentile(self.simulation_df.iloc[i], [1, 99]) for i in range(self.nr_of_days)])

        # Plot the results
        plt.figure(figsize=(20, 10))
        plt.plot(forecast_dates, mean_price, label='Mean Price', color='blue', linestyle='-', linewidth=2)

        # Annotate values
        for date, price in zip(forecast_dates, mean_price):
            plt.text(date, price, f'{price:.2f}', ha='center', va='bottom') 

        # Plot Confidence Intervals, using the transposed CI data
        plt.fill_between(forecast_dates, ci_90[:, 0], ci_90[:, 1], color='blue', alpha=0.2, label='90% Confidence Interval')
        plt.fill_between(forecast_dates, ci_95[:, 0], ci_95[:, 1], color='green', alpha=0.2, label='95% Confidence Interval')
        plt.fill_between(forecast_dates, ci_98[:, 0], ci_98[:, 1], color='red',  alpha=0.2, label='98% Confidence Interval')

        # Labels and title
        plt.title(f"Monte Carlo Simulation: {self.ticker} Stock Price with Confidence Intervals 90, 95 and 98")
        plt.xlabel('Date')
        plt.ylabel('Predicted mean/CI ($)')
        plt.xticks(rotation=90)  
        plt.legend()
        plt.tight_layout()
        plt.show()


    def simulation_plot(self):
        self.simulation_df.plot(legend=False, figsize=(15, 6))
        plt.suptitle(f'Monte Carlo Simulation result for: {self.ticker}')
        forecast_dates = pd.date_range(start=self.end_date, periods=self.nr_of_days + 1, freq='B')[1:]  # Skip the start date and generate business days
        # Set the x-ticks to be the forecast dates
        plt.xticks(ticks=np.arange(num_days), labels=forecast_dates.strftime('%Y-%m-%d'))
        plt.xticks(rotation=90)
        plt.axhline(y=self.last_price, color='red', linestyle='--', label=f'Last Price: {self.last_price}')
        plt.xlabel('Day')
        plt.ylabel('Price')
        plt.grid(True)
        plt.show()


    def plot_stock_data_column(self, column):
        plt.figure(figsize=(15, 6))
        plt.plot(self.data[column], label=f'{column}')
        plt.title(f'{column} of {self.ticker} Since {self.start_date} to {self.end_date}')
        plt.xlabel('Date')
        plt.ylabel(f'{column}')
        plt.legend()
        plt.grid(True)


# Execute Monte Carlo simulatiion using Monte_Carlo_Sim class
# Define your list of tickers
tickers = ["TSLA"]

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
for ticker in tickers:
    simulation = Monte_Carlo_Sim(ticker, start_date, end_date, 10, 5000)
    simulation.calculate_percentile_price_for_days()
    simulation.simulation_plot()
    simulation.plot_CI_price()
    simulation.plot_stock_data_column('Close')
    simulation.plot_stock_data_column('Volume')
