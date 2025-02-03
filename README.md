# Monte Carlo Simulation for Stock Price Prediction
This project uses the **Monte Carlo simulation** method to predict the future stock prices of **Tesla (TSLA)**. The simulation is based on historical daily returns and models the possible future price paths. The goal of the simulation is to generate multiple random price paths and estimate the potential future range of Tesla's stock price over a short time horizon.

## Features

- **Data Download**: Downloads historical stock data for Tesla from Yahoo Finance (yfinance).
- **Daily Return Calculation**: Calculates the daily percentage change in stock prices.
- **Monte Carlo Simulation**: Simulates multiple future stock price paths based on historical returns.
- **Visualization**: Visualizes the simulated stock price paths and provides the expected price range (mean, 5th percentile, and 95th percentile).
- **Forecasting**: Generates a forecast of Tesla's stock price for the next 5 days.

## Requirements

To run this project, you will need the following Python packages:

- `yfinance` - For downloading stock data from Yahoo Finance.
- `numpy` - For numerical operations and simulations.
- `pandas` - For data manipulation and analysis.
- `matplotlib` - For plotting graphs.

You can install all dependencies by running:

```bash
pip install -r requirements.txt
```

## **Usage**
1. Clone the Repository:
```bash
git clone https://github.com/Poulami-Nandi/MonteCarloSimStockPred.git
cd tesla-stock-price-monte-carlo
```
2. Download and Preprocess Data:
In the script monte_carlo_simulation.py, the historical stock data for Tesla (TSLA) is downloaded using the yfinance library, and daily returns are calculated.

3. Run the Monte Carlo Simulation:
Once the data is prepared, run the simulation to predict Tesla's stock price for the next 5 days.

```bash
python monte_carlo_simulation.py
```
4. Visualize the Results:
The script will generate a plot of the Monte Carlo simulations, showing multiple simulated price paths for the next 5 days. The graph will also display the last known price (today’s closing price) and highlight the mean, 5th percentile, and 95th percentile predicted prices for the next 5 days.

```bash
python monte_carlo_simulation.py
```

Example Output
Monte Carlo Simulation Plot: A graph showing 1000 simulated price paths for Tesla stock over the next 5 days.
Summary Statistics:
* Mean predicted price for the next 5 days
* 98th percentile predicted price (lower bound)
* 95th percentile predicted price (upper bound)

## **Directory Structure**
```bash
tesla-stock-price-monte-carlo/
│
├── data/                         # Contains raw and processed data
│   ├── tesla_stock_data.csv      # Raw data of Tesla stock (from Yahoo Finance)
│
├── scripts/                      # Python scripts for running the simulation
│   ├── Monte_Carlo_Simulation_stock_prediction.py # Script for performing the Monte Carlo simulation and plotting results
|
├── notebooks/
|   ├── Monte_Carlo_Simulation_stock_prediction.ipynb  # ipynb file for monte carlo simulation
│
├── requirements.txt              # List of required Python packages
├── README.md                     # Project overview and instructions
```

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.
