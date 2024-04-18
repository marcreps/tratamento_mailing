import requests

url = "https://www.cepaberto.com/api/v3/address"
# O seu token está visível apenas pra você
headers = {'Authorization': 'Token token=1f4a7325ee9c9e2c9cfd181fd9d3ab52'}
params = {'estado':'SP', 'cidade':'Praia Grande'}
response = requests.get(url, headers=headers, params=params)
#url = "https://www.cepaberto.com/api/v3/cities?estado=SP"
#response = requests.get(url, headers=headers)

print(response.json())