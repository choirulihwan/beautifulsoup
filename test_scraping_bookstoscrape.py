import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/page-1.html'
html_request = requests.get(url)

soup = BeautifulSoup(html_request.text, 'html.parser')
products = soup.find_all(attrs={'class':'product_pod'})
for product in products:
    print(product.find('h3').find('a').text)