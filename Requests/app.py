import requests

luck = 'people/1/'

request = requests.get(f'https://swapi.dev/api/{luck}')

print(request)  # response 200
print(dir(request))  # methods and attrs
print(request.headers)  # response in json format
print(request.json())  # response in json format
