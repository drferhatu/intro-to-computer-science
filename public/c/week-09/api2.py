# API → table → chart: the whole pipeline of a data job in 20 lines
# The hourly forecast for the next three days, as a DataFrame and a line chart

import matplotlib.pyplot as plt
import pandas as pd
import requests

params = {"latitude": 38.67, "longitude": 39.22, "hourly": "temperature_2m", "forecast_days": 3, "timezone": "Europe/Istanbul"}
response = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
response.raise_for_status()
hourly = response.json()["hourly"]                 # {"time": [...72 strings...], "temperature_2m": [...72 numbers...]}

df = pd.DataFrame(hourly)                          # a dict of lists is already a table
df["time"] = pd.to_datetime(df["time"])            # text → real dates
print(df.head())
print(f"min {df['temperature_2m'].min()} °C at {df.loc[df['temperature_2m'].idxmin(), 'time']}")

plt.plot(df["time"], df["temperature_2m"])
plt.title("Elazığ · temperature, next 72 hours")
plt.ylabel("°C")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
