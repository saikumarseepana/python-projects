import requests

response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
response.raise_for_status()

data = response.json()

longitude = data["longitude"]
latitude = data["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

print(response.json())