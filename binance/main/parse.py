import requests 
from bs4 import BeautifulSoup
from decimal import *


def view_information(name_coin):
	obj_list = {}
	url = 'https://coinmarketcap.com/currencies/{}/'
	link = requests.get(url.format(name_coin))
	soup = BeautifulSoup(link.text, 'lxml')

	name = soup.find('h2', class_='sc-1q9q90x-0 jCInrl h1').text
	price = float(soup.find('div', class_='priceValue').text[1::].replace(',', ''))
	market_cap = int(soup.find('div', class_='statsValue').text[1::].replace(',', ''))
	description = soup.find('div', class_='sc-2qtjgt-0 eApVPN')
	result = description.find('h2').text + '\n' + description.find('p').text

	obj_list['name'] = name 
	obj_list['price'] = price 
	obj_list['market_cap'] = market_cap 
	obj_list['description'] = description.text

	return obj_list

