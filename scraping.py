from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



url = 'https://cryptowat.ch/assets'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

#crypto_table = soup.find('table')

#rows = crypto_table.findAll('tr')

'''
for row in rows[:5]:
    cols = row.findAll('td')
    name = cols[2].text.strip()
    ticker = cols[1]
    c_price = float(cols[3].text)
    p_change = float(cols[5].text.strip('%'))

    s_price = round(c_price/(1+(p_change/100)),2)

    print(f"Name: {name}")
    print(f"Symbol: {ticker}")
    print(f"Current Price: {c_price}")
    print(f"24H Change: {p_change}")
    print(f"Starting Price: {s_price}")
'''