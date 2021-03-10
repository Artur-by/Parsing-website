"""Реализовать программу по сбору данных о товарах с сайта https://5element.by
Представить данные в текстовом файле outdata.txt (категория, название, цена, акционная цена)"""

import requests                 # импорт библиотеки Requests
from lxml import html           # импорт пакета для работы с HTML

url = 'https://sila.by/ntpk/aksessuary_apple'
response = requests.get(url=url)
response.encoding = 'cp1251'
tree = html.fromstring(response.text)


path = ["//div/sup[1]", "//a/span[1]/b[1]", "//a/span[1]/strong[1]", "//div[@class='price']/div[1]"]
# в списке path указаны патчи требуемых позиций

for e in path:                  # цикл по перебору патчей
    element = tree.xpath(e)
    q=[]
    for i in element:
        #print(i.text)          можно распечатать в столбец элементы
        q.append(i.text)
    print(q)
