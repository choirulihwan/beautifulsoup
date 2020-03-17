"""
author: choirul ihwan
deskripsi: gabungan antara web scrape dan flask
"""

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

#main program start here
@app.route('/')
def home():
    html_request = requests.get('https://www.ebay.com/sch/i.html',
                                params={'_from': 'R40', '_trksid': 'm570.l1313', '_nkw': 'iphone', '_sacat': '0'})
    soup = BeautifulSoup(html_request.text, 'html.parser')

    product_image = soup.find_all(attrs={'class': 's-item__image'})
    return render_template('index.html', images=product_image)


if __name__ == '__main__':
    app.run(debug=True)