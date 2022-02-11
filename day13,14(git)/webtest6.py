from bs4 import BeautifulSoup
import urllib.request as req
file=open("news.txt","wt",encoding="utf-8")
url = "https://news.daum.net"
result = req.urlopen(url)
soup = BeautifulSoup(result, "html.parser")
news = soup.select("strong.tit_g")
for list in news:
    a = list.select_one("a")
    print("링크 : " + a.get('href'))
    file.write("링크 : " + a.get('href')+'\n')
    title = a.string
    print("제목 : " + title.strip())
    file.write("제목 : " + title.strip()+'\n')
