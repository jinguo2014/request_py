import requests

url = 'http://b2b.htyyao.com/mobile/index.php'
data = {
    'act': 'index',
    'op': 'index'
}
response = requests.get(url, params=data)
print(response.url)
print(response.text)