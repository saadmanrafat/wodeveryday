import requests

endpoint = 'https://www.crossfit.com/cf/find-a-box.php?page=1&country=&state=&city=&type=Commercial'
response = requests.get(endpoint)
data = response.json()
affiliates = data['affiliates']

