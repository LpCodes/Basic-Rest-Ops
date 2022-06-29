from urllib import response
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)

print(response)

# m1 = ['apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

# for i in m1:
#     print(i)
#     print(getattr(response, i))
#     print("*"*140)

data = response.json()

print(data)

for x,y in data.items():
    print(x,y)



