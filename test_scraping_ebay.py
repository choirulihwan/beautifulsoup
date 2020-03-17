import requests
from bs4 import BeautifulSoup

#target
html_request = requests.get('https://www.ebay.com/sch/i.html', params={'_from':'R40', '_trksid':'m570.l1313', '_nkw':'iphone', '_sacat':'0'})
#print(html_request.text)

soup = BeautifulSoup(html_request.text, 'html.parser')
#print(soup)

product_image = soup.find_all(attrs={'class':'s-item__image'})
for img in product_image:
    print(img.find('img')['alt'])