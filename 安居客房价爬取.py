from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
}

url = 'https://www.anjuke.com/fangjia/guangdong2021/'

response_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(response_text)
li_list = tree.xpath('/html/body/div[2]/div[4]/div[1]/div[1]/ul/li')
fp = open('房价.txt', 'w', encoding='utf-8')
for li in li_list:
    name = li.xpath('./a/b/text()')[0]
    price = li.xpath('./a/span/text()')[0]
    increase = li.xpath('./a/em/text()')[0]
    content = name + ' ' + price + ' ' + increase + '\n'
    fp.write(content)
fp.close()
