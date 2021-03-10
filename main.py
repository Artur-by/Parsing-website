import requests
from lxml import html

url = 'https://www.21vek.by/bathtubs/'
response = requests.get(url=url)

xpath = '//*[@id="5904035"]/div/span[3]/span[1]'
tree = html.fromstring(response.text)

for index in range(1, 15):
    xpath_1 = f'//*[@id="j-result-page-1"]/li[{index}]/dl/div[2]/span[1]/span[2]'
    element = tree.xpath(xpath_1)
    text = element[0].text
    if text == 'р.':
        xpath_2 = f'//*[@id="j-result-page-1"]/li[{index}]/dl/div[2]/span[1]/span[1]'
        element = tree.xpath(xpath_2)
        text = element[0].text
    print(text)

xpath = "//li/dl[1]/div[@class='catalog-result__item_data' and 1]/dt[@class='result__root' and 1]/a[@class='result__link j-ga_track' and 1]/span[@class='result__name' and 2]"
element = tree.xpath(xpath)
a = []
for e in element:
    a.append(e.text)

print(a)