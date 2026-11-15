# One request to a web API: a URL goes out, JSON comes back
# pip install requests

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=38.67&longitude=39.22&current=temperature_2m,wind_speed_10m"

response = requests.get(url, timeout=10)

print(response.status_code)        # 200 means OK; 404 not found; 429 too many requests; 500 their problem
data = response.json()             # JSON text → Python dicts and lists
print(data.keys())
print(data["current"])
print(f"Elazığ now: {data['current']['temperature_2m']} °C, wind {data['current']['wind_speed_10m']} km/h")
