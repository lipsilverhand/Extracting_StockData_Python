import yfinance as yf
import pandas as pd
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
response = requests.get(url)
data = response.json()


country = data['country']
sector = data['sector']

print(f"Country: {country}")  
print(f"Sector: {sector}")   

amd = yf.Ticker("AMD")
amd_history = amd.history(period="max")

first_day_volume = amd_history['Volume'].iloc[0]

print(f"Volume traded on the first day: {first_day_volume}")
