import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

datatosend = {"userId": 2, "title": "lll", "completed": False}

response = requests.post(api_url, json=datatosend)

print(response)

data = response.json()


for i in data.items():
    print(i)

api_url = "https://jsonplaceholder.typicode.com/todos"

response_list = requests.get(api_url).json()



for i in response_list:
    print(i['title'])



