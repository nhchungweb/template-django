import requests

url = 'http://127.0.0.1:8000/api/cars'
headers = {'Authorization': 'Token 220a75a037a3b6fd42f7bcb4f9007d2916279fc9'}
r = requests.get(url, headers=headers)

print(r.text)