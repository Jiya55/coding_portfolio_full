from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.polygon.io/"
API_KEY= "fIy5VaPyxxzzY3kOS0rU88YI1S1FrdKg"

printer = PrettyPrinter()
def get_stocks():
   endpoint = f"v3/reference/tickers?market=stocks&active=true&sort=ticker&order=asc&limit=20&apiKey={API_KEY}"
   url = BASE_URL + endpoint
   data = get(url).json()['results']
   stock_listing ={}
   for stock in data:
       stock_listing[stock['name']] ={
        'place':stock['locale'], 
       'ticker':stock['ticker'],
       'primary exchange':stock['primary_exchange'],
       #Central Index Key....is this imp,,, if it is de comment below code
       #'CIK':stock['cik']#, code not working....key error same with type
       }
   return stock_listing
def print_stocks(stocks):
    for stock in stocks:
        place=stocks[stock]['place']
        ticker=stocks[stock]['ticker']
        exchange=stocks[stock]['place']
        print(f'{stock} : market:{place},  ticker(symbol):{ticker},  primary exchnage:{exchange}\n')
#make this more good looking rn it just rints the dict
def property_checker(prop, keys):
    if prop in keys:
        return True
    else:
        return False
def stock_description(ticker):
    endpoint = f"v3/reference/tickers/{ticker}?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    if property_checker('name', data.keys()):
        print(data['name'])
    if property_checker('description', data.keys()):
        print(data['description'])
    if property_checker('cik', data.keys()):
        print('cik: '+data['cik'])   
    if property_checker('homepage_url', data.keys()):
        print('website: '+data['homepage_url'])
    if property_checker('locale', data.keys()):
        print('locale: '+data['locale']) 
    if property_checker('market', data.keys()):
        print('market: '+data['market']) 
    if property_checker('market_cap', data.keys()):
        print('market capital(recent close price of the ticker multiplied by weighted outstanding shares): '+str(data['market_cap']))
    if property_checker('primary_exchange', data.keys()):
        print('primary exchange: '+data['primary_exchange'])
    if property_checker('type', data.keys()):
        if data['type']=='CS':
            print('type of share: Common Stock')
        else:
            print('type of share: '+data['type'])
def stock_details(ticker, multiplier, timespan):
    endpoint=f'v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/2022-06-06/2022-06-06?adjusted=true&sort=asc&limit=120&apiKey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()["results"][0]#there are two dict
    if property_checker('c', data.keys()):
        print('the closing price for the given time period is: '+str(data['c']))
    if property_checker('h', data.keys()):
        print('the highest price for the given time period is: '+str(data['h']))
    if property_checker('l', data.keys()):
        print('the highest price for the given time period is: '+str(data['l']))
    if property_checker('n', data.keys()):
        print('the number of transactions for the given time period is: '+str(data['n']))
    if property_checker('o', data.keys()):
        print('the opening price for the given time period is: '+str(data['o']))
    if property_checker('v', data.keys()):
        print('the trading volume for the given time period is: '+str(data['v']))
    if property_checker('vw', data.keys()):
        print('the volume weighted average price for the given time period is: '+str(data['n']))

stocks= get_stocks()
stock_details('AAPL', '1', 'day')





