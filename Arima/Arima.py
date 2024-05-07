import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

file_path = "balance_data.xlsx"
df = pd.read_excel(file_path)

time_series_data = df[['Year', 'Date', 'Nature of injury']]

time_series_data['Date'] = pd.to_datetime(time_series_data['Date'], format='%B %d, %Y')
time_series_data.set_index('Date', inplace=True)


time_series_data_resampled = time_series_data.resample('M').count()
time_series_data_resampled.index.freq = 'M'

# # Plot the time series
# plt.figure(figsize=(12, 6))
# plt.plot(time_series_data_resampled.index, time_series_data_resampled['Nature of injury'], label='Nature of injury')
# plt.title('Monthly Time Series - Nature of Injury')
# plt.xlabel('Date')
# plt.ylabel('Count')
# plt.legend()
# plt.show()


model = ARIMA(time_series_data_resampled['Nature of injury'], order=(10,1,9))  # You may need to tune these parameters
result = model.fit()

forecast_steps = 12  # Adjust as needed
forecast = result.get_forecast(steps=forecast_steps)

# Plot the original time series and the forecast
plt.figure(figsize=(12, 6))
plt.plot(time_series_data_resampled.index, time_series_data_resampled['Nature of injury'], label='Actual')
plt.plot(pd.date_range(start=time_series_data_resampled.index[-1], periods=forecast_steps + 1, freq='M')[1:], forecast.predicted_mean, label='Forecast', linestyle='--')
plt.title('Time Series Forecasting - Nature of Injury')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()
