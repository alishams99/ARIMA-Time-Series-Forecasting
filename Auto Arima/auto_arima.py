import pandas as pd
import matplotlib.pyplot as plt
from pmdarima import auto_arima

file_path = "balance_data.xlsx"
df = pd.read_excel(file_path)

time_series_data = df[['Year', 'Date', 'Nature of injury']]
time_series_data['Date'] = pd.to_datetime(time_series_data['Date'], format='%B %d, %Y')
time_series_data.set_index('Date', inplace=True)
time_series_data_resampled = time_series_data.resample('M').count()
time_series_data_resampled.index.freq = 'M'


model = auto_arima(time_series_data_resampled['Nature of injury'], seasonal=True, m=12)

# Forecast for the next 5 years (60 months)
forecast_steps = 60
forecast, conf_int = model.predict(n_periods=forecast_steps, return_conf_int=True)


plt.figure(figsize=(12, 6))

plt.plot(time_series_data_resampled.index, time_series_data_resampled['Nature of injury'], label='Historical Data')

forecast_index = pd.date_range(start=time_series_data_resampled.index[-1], periods=forecast_steps + 1, freq='M')[1:]
plt.plot(forecast_index, forecast, label='Forecast', linestyle='--', color='green')
plt.fill_between(forecast_index, conf_int[:, 0], conf_int[:, 1], color='green', alpha=0.2)

plt.title('Time Series Forecasting - Nature of Injury')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()
