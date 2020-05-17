import urllib2
# handler = urllib2.HTTPHandler(debuglevel = 1)
from bs4 import BeautifulSoup

req = urllib2.Request('https://haji.kemenag.go.id/v4/estimasi-keberangkatan')
req.add_header('Cookie', ("nomor_porsi=1200087878"))

# opener = urllib2.build_opener(handler)
# urllib2.install_opener(opener)

resp = urllib2.urlopen(req)
# print(resp.read())

soup = BeautifulSoup(resp, 'html.parser')
data = soup.find_all('td')
# print(data)
# print('Nomor porsi: {}'.format(data[8].get_text()))
data_haji = {}
data_haji['nomor_porsi'] = data[8].get_text()
print(data_haji)
