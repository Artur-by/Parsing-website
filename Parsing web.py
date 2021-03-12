"""Реализовать программу по сбору данных о товарах с сайта https://5element.by
Представить данные в текстовом файле outdata.txt (категория, название, цена, акционная цена)"""

import requests  # импорт библиотеки Requests
from lxml import html  # импорт пакета для работы с HTML

path_tipe = '//a/span[1]/b[1]'
path_name = '//a/span[1]/strong[1]'
path_code = '//div/sup[1]'
path_price_rub = "//div[@class='price']/div[1]/b[1]"
path_price_kop = "//div[@class='price']/div[1]/b[2]"


def append_file(name_file, value):  # функция записи в файл
    file = open(name_file, 'a')
    file.write(value + '\n')
    file.close()

def readlines_file(name_file):  # функция чтения файла
    file = open(name_file, 'r')
    date = file.readlines()
    file.close()
    return date


def parsing(urllink, pagelink):                # функция парсинга категории товара
    for i in range (1, pagelink+1):              # цикл по перебору страниц мобильных устройств
        url = urllink+'/page/'+str(i)

        response = requests.get(url=url)
        response.encoding = 'cp1251'
        tree = html.fromstring(response.text)

        el_tipe = tree.xpath(path_tipe)     # парсим список типов устройств
        a_tipe = []
        for i in el_tipe:
            a_tipe.append(i.text)
        #print(a_tipe)

        el_name = tree.xpath(path_name)     # парсим название устройств
        a_name = []
        for i in el_name:
            a_name.append(i.text)

        el_code = tree.xpath(path_code)     # парсим коды устройств
        a_code = []
        for i in el_code:
           a_code.append(i.text)

        el_price_rub = tree.xpath(path_price_rub)   # парсим цену устройств-рубли
        a_price_rub = []
        for i in el_price_rub:
            a_price_rub.append(i.text)

        el_price_kop = tree.xpath(path_price_kop)  # парсим цену устройств-копейки
        a_price_kop = []
        for i in el_price_kop:
            a_price_kop.append(i.text)

        item = []                           # создаем новый список тип+название+код+цена устройства
        for i in range(len(a_tipe)):
            item.append(a_tipe[i]+' ' + a_name[i]+' ' + a_code[i] +' '+ a_price_rub[i]+','+a_price_kop[i]+' руб.')

        for i in item:                      # новый список разбиваем построчно и записываем в файл
            print(i)
            append_file('mobil.txt', i)



spis = readlines_file('ntkp_url.txt')   # перебираем адреса из файла со списком url и передаем в функцию парсинга
for i in spis:
    spisOne = i.split(';\n')
    for j in spisOne:
        spisToo = j.split(',')
        if j !='':
            parsing(spisToo[1], int(spisToo[2]))    # парсим каждую группу товаров



