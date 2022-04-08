import requests
import json

def test_url():
	astros = requests.get('http://api.open-notify.org/astros.json')
	data = astros.text
	file = open("data.json", "w")
	load_data = json.loads(file)
	file.write(json.dumps(load_data, sort_keys=True, indent=4))
	if astros.status_code != 200:
    # This means something went wrong.
		print(f"Astros Status Code - ", astros.status_code)