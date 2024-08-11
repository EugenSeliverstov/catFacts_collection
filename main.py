# Запрос на отображение 2 пород котиков на странице:

import requests
base_url = "https://catfact.ninja"
endpoint = "/breeds"
query_params = {'limit': 2}
response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)

# Запрос на отображение рандомного факта о котиках, максимальной длиной 30 знаков:

import requests
base_url = "https://catfact.ninja"
endpoint = "/fact"
query_params = {'max_length': 30}
response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)

# Запрос на отображение списка фактов о котиках (макс. длина - 50 знаков, количество - 2)

import requests
base_url = "https://catfact.ninja"
endpoint = "/facts"
query_params = {
    'max_length': 50,
    'limit': 3
}
response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)
