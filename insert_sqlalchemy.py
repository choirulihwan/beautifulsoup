import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import requests
from bs4 import BeautifulSoup
from slugify import slugify

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:bermutu@192.168.10.3:3306/db_python', echo=True)

Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(length=100))
    slug = sqlalchemy.Column(sqlalchemy.String(length=150))
    price = sqlalchemy.Column(sqlalchemy.Numeric(precision=10, scale=2))
    image = sqlalchemy.Column(sqlalchemy.String(length=100))

    def __repr__(self):
        return "Judul: {0}, Harga: {1}".format(self.title, self.price)

Base.metadata.create_all(engine)

#create session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# Add a book
#obj_book = Books(id=1, title='test', slug='test', price=10, image='http://www.test.com/1.jpg')
#session.add(obj_book)
#session.commit()

#scrap book
jml_hal = 50

for x in range(jml_hal):
    url = 'http://books.toscrape.com/catalogue/page-' + str(x) + '.html'
    html_request = requests.get(url)

    soup = BeautifulSoup(html_request.text, 'html.parser')
    books = soup.find_all(attrs={'class':'product_pod'})

    for book in books:
        judul = book.find('h3').find('a')['title']
        slug = slugify(judul)
        harga = book.find(attrs={'class':'product_price'}).find(attrs={'class':'price_color'}).text
        harga = float(harga[2:])
        gambar = book.find(attrs={'class':'image_container'}).find('a').find('img')['src']
        gambar = gambar.replace('..', 'http://books.toscrape.com')

        obj_book = Books(title=judul, slug=slug, price=harga, image=gambar)
        session.add(obj_book)

session.commit()
