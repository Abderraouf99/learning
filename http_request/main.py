import requests

try:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    response = response.json()
    print(response)
except:
    print("Failed to fetch the data")
