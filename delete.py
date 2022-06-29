from urllib import response
import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(api_url)

print(response)

# m1 = ['apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

# for i in m1:
#     print(i)
#     print(getattr(response, i))
#     print("*"*140)

data = response.json()

print(data)

for i in data:
    print(i)
    api_url = f"https://jsonplaceholder.typicode.com/todos/{i['userId']}"
    response = requests.delete(api_url)
    print(response.status_code)
    print(response.json())



