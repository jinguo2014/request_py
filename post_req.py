import requests

url = 'http://b2b.htyyao.com/mobile/index.php?act=login&op=loginByUsername'
data = {
    'client': 'android',
    'username': 'jinguo1988',
    'password': '123456'
}
response = requests.post(url, data=data)
print(response.text)





