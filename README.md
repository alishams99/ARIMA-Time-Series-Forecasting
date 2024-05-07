# Time Series Forecasting with ARIMA Model

## Overview

This repository contains Python code for time series forecasting using the ARIMA (AutoRegressive Integrated Moving Average) model. The primary script `arima.py` utilizes the `pandas`, `matplotlib`, and `pmdarima` libraries to perform forecasting on a provided dataset.

The dataset (`balance_data.xlsx`) is a sample dataset containing information about the "Nature of Injury" over time. Please note that this dataset is for demonstration purposes only and contains only 1000 rows of data.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine using `git clone https://github.com/alishams99/ARIMA-Time-Series-Forecasting.git`.
3. Navigate to the project directory.
4. Install the required dependencies by running `pip install -r requirements.txt`.
5. Run the `arima.py` script to perform time series forecasting using the ARIMA model.

## Description

The `auto_arima.py` script performs the following steps:

1. Reads the dataset from the provided Excel file (`balance_data.xlsx`) using `pandas`.
2. Prepares the time series data by resampling it to monthly frequency.
3. Fits an ARIMA model to the resampled time series data using `auto_arima` from `pmdarima`.
4. Forecasts the future values of the time series for the next 5 years (60 months).
5. Plots the historical data along with the forecasted values and confidence intervals using `matplotlib`.

## Files

- `balance_data.xlsx`: Sample dataset containing time series data.
- `requirements.txt`: List of required Python packages and their versions.

## Results

The script generates a plot displaying the historical data along with the forecasted values and confidence intervals for the "Nature of Injury" over time.

## Note

- The dataset provided (`balance_data.xlsx`) is for demonstration purposes only and contains only 1000 rows of data.
- Adjustments may be required in the script for working with larger datasets or different data formats.
