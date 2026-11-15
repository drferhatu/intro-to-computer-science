# The same request, written the way real code writes it:
# parameters in a dict, a function, and every way it can fail handled

import sys

import requests

CITIES = {"Elazığ": (38.67, 39.22), "İstanbul": (41.01, 28.98), "Ankara": (39.93, 32.86), "Houston": (29.76, -95.37)}


def current_weather(latitude, longitude):
    """Return the current temperature (°C) and wind speed (km/h) at a location."""
    params = {"latitude": latitude, "longitude": longitude, "current": "temperature_2m,wind_speed_10m"}
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
    response.raise_for_status()                    # turn a 4xx/5xx answer into an exception
    current = response.json()["current"]
    return current["temperature_2m"], current["wind_speed_10m"]


def main():
    for city, (lat, lon) in CITIES.items():
        try:
            temperature, wind = current_weather(lat, lon)
        except requests.exceptions.Timeout:
            print(f"{city:10} the server did not answer in 10 seconds")
        except requests.exceptions.ConnectionError:
            sys.exit("No internet connection.")
        except requests.exceptions.HTTPError as error:
            print(f"{city:10} the server refused: {error}")
        else:
            print(f"{city:10} {temperature:5.1f} °C   wind {wind:4.1f} km/h")


if __name__ == "__main__":
    main()
