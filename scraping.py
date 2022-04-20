from unicodedata import name
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



url = 'https://www.coingecko.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print()

print('-' * 67)

print(' ' + title.text)

print('-' * 67)

print()

crpyto_table = soup.findAll('tbody')

crpyto_table = crpyto_table[0]

table_rows = crpyto_table.findAll('tr')

for row in table_rows[:5]:
    cols = row.findAll("td")
    name = cols[2].find("a",attrs={'class':"tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between"})
    name = name.text.strip()
    ticker = cols[2].find("span",attrs={'class':"tw-hidden d-lg-inline font-normal text-3xs ml-2"})
    ticker = ticker.text.strip()
    price = cols[4].text.strip('\n$')
    price_float = float(price.replace(',',''))
    twofour_delta1 = cols[6].text.strip()
    twofour_delta2 = float(twofour_delta1.strip('%'))
    twofour_price = round(price_float/(1+(twofour_delta2/100)),2)

    twofour_price = "{:,.2f}".format(twofour_price)

    print(f"Name:      {name}")
    print(f"Ticker:    {ticker}")
    print(f"Price:     ${price}")
    print(f"24H \u0394:     {twofour_delta1}")
    print(f"24H Price: ${twofour_price}")
    print()