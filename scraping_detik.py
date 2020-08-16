import requests
from bs4 import BeautifulSoup

target = 'https://www.detik.com/terpopuler'
html = requests.get(target, params={'tag_from':'wp_cb_mostPopular_more'})



soup = BeautifulSoup(html.text, "html.parser")

articles = soup.find(attrs={"class":"grid-row list-content"})

titles = articles.find_all(attrs={"class":"media__title"})

for title in titles:
    print(title.text)