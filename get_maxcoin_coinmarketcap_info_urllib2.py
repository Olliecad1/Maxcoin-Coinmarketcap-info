# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

## Importing Required modules
import urllib2
import json

## url variable equals to api
url = "https://api.coinmarketcap.com/v1/ticker/maxcoin/?convert=GBP"

## Opening or Connecting to the url
s = urllib2.urlopen(url)

## Reading the data
s = s.read()

## converting the data to string
j = str(s)

# converting to json
j = json.loads(j)

## name
GetName = j[0]['name']

## ranks on coinmarketcap
rank = j[0]['rank']

## price in usd
price_usd = j[0]['price_usd']

## price in bitcoin
price_btc = j[0]['price_btc']

## price in gbp
price_gbp = j[0]['price_gbp']

## Market cap in gbp
market_cap_gbp = j[0]['market_cap_gbp']

## Market cap in usd
market_cap_usd = j[0]['market_cap_usd']

## Printing name
print 'Name: ' + GetName

## Printing rank
print 'Rank: ' + rank

print 'MaxCoin Price in USD: ' + '$' + price_usd

print 'MaxCoin Price in BTC: ' + price_btc

print 'MaxCoin Price in GBP: ' + '£' + price_gbp


