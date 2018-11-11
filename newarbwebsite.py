
import requests
import json
import time
import math
import re

class getcrypto:
    def __init__(self, exchange, pair):
        self.exchange = exchange
        self. pair = pair

    def getbidaskdata(self):

        r = requests.get('https://api.cryptowat.ch/markets/' + self.exchange + '/' + self.pair + '/orderbook')
        #print(r.text)
        q = str(r.text)
        parsed_json = json.loads(q)

        exchange = self.exchange
        pair = self.pair
        self.ask = (parsed_json['result']['asks'][0][0])
        self.bid = (parsed_json['result']['bids'][0][0])
        self.spread = self.ask - self.bid
        return(self.pair, self.ask, self.bid, self.spread)

    def getkucoin(self):
        d = requests.get('https://api.kucoin.com/v1/LTC-BTC/open/orders-buy/')
        #print(d.text)
        q = str(d.text)
        parsed_json = json.loads(q)

        self.bid = (parsed_json['data'][0][0])
        return self.bid

    def getbitmex(self):
        e = requests.get('https://www.bitmex.com/api/v1/orderBook/L2?symbol=ltc&depth=10')
        f = str(e.text)
        parsed_json = json.loads(f)
        self.ask = (parsed_json[0]['price'])
        return self.ask

crypto1 = getcrypto('poloniex', 'ltcbtc')
crypto2 = getcrypto('binance', 'ltcbtc')
kucoinobj = getcrypto('kucoin', 'ltcbtc')
crypto4 = getcrypto('kraken', 'ltcbtc')
crypto5 = getcrypto('poloniex', 'ltcbtc')
crypto6 = getcrypto('binance', 'ltcbtc')

bitmexobj = getcrypto('bitmex', 'ltc')
crypto1.getbidaskdata()
crypto2.getbidaskdata()
crypto4.getbidaskdata()
crypto5.getbidaskdata()
crypto6.getbidaskdata()
bitmexobj.getbitmex()
kucoinobj.getkucoin()
#crypto7.getkucoin()
mothercryptoarray = [crypto1.ask, bitmexobj.ask]
childcryptoarray = [crypto1.bid, kucoinobj.bid, crypto2.bid, crypto4.bid, crypto5.bid, crypto6.bid]


#currently missing two items from child array for some reason
print('mother array')
print(mothercryptoarray)
print('child array')
print(childcryptoarray)
print('Raw Profit Mother - child array')
rawexchangespread = (max(mothercryptoarray) - min(childcryptoarray))
print(rawexchangespread)
exchangecost = max(mothercryptoarray)*(.00175)
print('exchange fees')
print(exchangecost)
possibleprofit = rawexchangespread - exchangecost
print('Possible Actual Profit')
print(possibleprofit)

# totalpotentialprofit = -5
# while True:
#     if totalpotentialprofit <= 0:
#
#         print(crypto1.getbidaskdata())
#         print(crypto2.getbidaskdata())
#         kucoinobj.getkucoin()
#         exchangefee = crypto1.bid*.00175*4
#
#         #print('inter-exchange spread ' + str((crypto1.ask - crypto2.bid )))
#         #print('exchange fee ' + str(exchangefee))
#         print('*******************************************************')
#         totalpotentialprofit2 = (crypto1.ask - kucoinobj.ask) - exchangefee
#         totalpotentialprofit = (crypto1.ask - crypto2.bid) - exchangefee
#         print('total potential profit ' + str(totalpotentialprofit))
#         print('--------------------------------------------------------------------------------')
#         print(totalpotentialprofit2)
#         print('--------------------------------------------------------------------------------')
#         time.sleep(10)
#     else:
#         print(str(totalpotentialprofit))
#         break
