import urllib2
# handler = urllib2.HTTPHandler(debuglevel = 1)
from bs4 import BeautifulSoup


def scrap_haji(no_porsi):
    url = 'https://haji.kemenag.go.id/v4/estimasi-keberangkatan'
    ls_cookie = 'nomor_porsi=' + no_porsi

    req = urllib2.Request(url)
    req.add_header('Cookie', (ls_cookie))

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
    # print(data_haji)
    return data_haji

print(scrap_haji('1200087878'))