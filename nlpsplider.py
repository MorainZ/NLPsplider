# -*-coding:utf-8-*-
from bs4 import BeautifulSoup


import requests
import pdfcrowd


base_url = "http://www.threedweb.cn/thread-1282-1-1.html"

def saveHtml(data):
    res = requests.get(data["href"])
    soup = BeautifulSoup(res.text,"html.parser")
    # contents = soup.findAll(class_="t_f", limit=1)
    contents = soup.findAll(class_="t_f", limit=1)
    for content in contents:
        with open(data["title"] + ".html", "wb") as f:
            f.write(content.encode("utf-8"))
    # print(content.name)
    # print(content.div)
    # soup_text = BeautifulSoup(str(content), 'lxml')
    # # 将\xa0无法解码的字符删除
    # print(soup_text.div.text.replace('\xa0', ''))
    # fileHandle = open("qiushibaike2.txt", 'a')
    # fileHandle.write(content)
    # fileHandle.write("\n")
    output_file = open(data["title"] + '.pdf', 'wb')
    client.convertFile(data["title"] + '.html', output_file)
    output_file.close()

# create an API client instance
client = pdfcrowd.Client("morningrain", "12ab704789a57360d41232b313ed80ed")

res = requests.get(base_url)
soup = BeautifulSoup(res.text,"html.parser")
contents = soup.select(".t_f > a")
for content in contents:
    data = {
        'title':content.text,
        'href': content.get('href')
    }
    print(data)
    saveHtml(data)



