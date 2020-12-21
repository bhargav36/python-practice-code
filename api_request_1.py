import requests
import json

parameter = { "lat": 40.71, "lon": -74}

astros = requests.get('http://api.open-notify.org/astros.json')
iss = requests.get("http://api.open-notify.org/iss-pass.json", params = parameter)


if astros.status_code != 200 or iss.status_code != 200:
    # This means something went wrong.
    print(f"Astros Status Code - ", astros.status_code )
    print(f"ISS Status Code - ", iss.status_code )
# Function to print json data
def jsonprint(obj):
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)

jsonprint(astros.json())
jsonprint(iss.json())