import requests

# put is used to replace exiting data

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()


todo = {"userId": 176, "title": "bb", "completed": True}
response = requests.put(api_url, json=todo)
print(response.status_code)
print(response.json())


# requests.patch() to modify the value of a specific field on an existing todo. PATCH differs from PUT in that it doesn’t completely replace the existing resource. It only modifies the values set in the JSON sent with the request.

todo = {"title": "Mow lawn",'userId':323}
response = requests.patch(api_url, json=todo)
print(response.status_code)
print(response.json())
