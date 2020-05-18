import requests

app_key = '851afb25a4e5892c83effaca8de17c5c'
diy = '1621176'
yogya = '1621177'
bantul = '1650119'
sleman = '1626754'

url = 'http://samples.openweathermap.org/data/2.5/weather?id=' + diy + '&appid=' + app_key
response = requests.get(url)
result = response.json()

print(result)