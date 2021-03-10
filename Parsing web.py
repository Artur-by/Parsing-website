"""Реализовать программу по сбору данных о товарах с сайта https://5element.by
Представить данные в текстовом файле outdata.txt (категория, название, цена, акционная цена)"""

import requests                 # импорт библиотеки Requests
from lxml import html           # импорт пакета для работы с HTML

url = 'https://sila.by/ntpk/aksessuary_apple'
response = requests.get(url=url)
response.encoding = 'cp1251'
tree = html.fromstring(response.text)


path_name = "//a/span[1]/b[1]"
path_fullname = "//a/span[1]/strong[1]"
path_code = "//div/sup[1]"
path_price ="//div[@class='price']/div[1]"



el_name = tree.xpath(path_name)
print(len(el_name))
a_name = []
for i in el_name:
    a_name.append(i.text)
print(a_name)

el_fullname = tree.xpath(path_fullname)
print(len(el_fullname))
a_fullname = []
for i in el_fullname:
    a_fullname.append(i.text)
print(a_fullname)

el_code = tree.xpath(path_code)
print(len(el_code))
a_code = []
for i in el_code:
    a_code.append(i.text)
print(a_code)

el_price = tree.xpath(path_price)
print(len(el_price))
a_price = []
for i in el_price:
    a_price.append(i.text)
print(a_price)

'''for index in range(1, 5):
    path_price = "//div[@class='price']/div[1]"
    element = tree.xpath(path_price)
    text = element[0].text
    print(text)'''

