import bs4
import requests

# bantul
url = 'http://jadwalsholat.pkpu.or.id/?id=25'
content = requests.get(url)

response = bs4.BeautifulSoup(content.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
hasil = data[0]

sholat = {}
i = 0
for h in hasil:
    if i == 1:
        sholat['shubuh'] = h.get_text()
    elif i == 2:
        sholat['dzuhur'] = h.get_text()
    elif i == 3:
        sholat['ashar'] = h.get_text()
    elif i == 4:
        sholat['maghrib'] = h.get_text()
    elif i == 5:
        sholat['isya'] = h.get_text()
    i += 1

print(sholat)