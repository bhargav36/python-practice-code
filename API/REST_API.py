import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Sell milk"}

response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)

