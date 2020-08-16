import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index_detik.html')

@app.route('/detik')
def detik():
    target = 'https://www.detik.com/terpopuler'
    html = requests.get(target, params={'tag_from': 'wp_cb_mostPopular_more'})

    soup = BeautifulSoup(html.text, "html.parser")

    articles = soup.find(attrs={"class": "grid-row list-content"})

    titles = articles.find_all(attrs={"class": "media__title"})
    images = articles.find_all(attrs={"class": "media__image"})

    list_title = []
    for title in titles:
        list_title.append(title.text)

    list_url = []
    list_image = []
    for image in images:
        url = image.find('a')['href']
        list_url.append(url)
        src = image.find('img')['src']
        list_image.append(src)


    return render_template('index_detik.html', images=list_image, titles=list_title, urls=list_url, judul="Detik")


@app.route('/viva')
def viva():
    target = 'https://www.viva.co.id/trending'
    html = requests.get(target)

    soup = BeautifulSoup(html.text, "html.parser")

    articles = soup.find(attrs={"class": "modlist-1"})

    titles = articles.find_all(attrs={"class": "title-content"})
    images = articles.find_all(attrs={"class": "thumb"})

    list_title = []
    for title in titles:
        list_title.append(title.find('h3').text)

    list_url = []
    list_image = []
    for image in images:
        url = image.find(attrs={"class": "flex_lazy"})['href']
        list_url.append(url)
        src = image.find('img')['src']
        list_image.append(src)


    return render_template('index_detik.html', images=list_image, titles=list_title, urls=list_url, judul='Viva News')


@app.route('/liputan6')
def liputan6():
    target = 'https://www.liputan6.com/indeks/terpopuler'
    html = requests.get(target)

    soup = BeautifulSoup(html.text, "html.parser")

    articles = soup.find(attrs={"class": "articles--list"})

    titles = articles.find_all(attrs={"class": "articles--rows--item__title-link-text"})
    images = articles.find_all(attrs={"class": "articles--rows--item"})

    list_title = []
    for title in titles:
        list_title.append(title.text)


    list_url = []
    list_image = []
    for image in images:

        # pass
        url = image.find(attrs={"data-template-var": "url"})['href']
        list_url.append(url)
        src = image.find('img')['src']
        list_image.append(src)

    return render_template('index_detik.html', images=list_image, titles=list_title, urls=list_url, judul='Liputan 6')





if __name__ == '__main__':
    app.run(debug=True)