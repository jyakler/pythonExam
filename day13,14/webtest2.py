from bs4 import BeautifulSoup
html = """
<html>
    <head>
        <title>파이썬 웹 크롤링</title>
    </head>
    <body>
        <h1 id="title">안녕하세요</h1>
        <h1>test</h1>
        <p id="name">정수아입니다</p>
        <ul>
            <li><a href="http://www.naver.com">네이버</a></li>
            <li><a href="http://www.google.com">구글</a></li>
        </ul>
    </body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
title = soup.find("h1")
name = soup.find(id="name")
print("title : " + title.string)
print("name : " + name.string)
list=soup.find_all("a")
for a in list:
    text=a.string
    print(text)
print()
#attrs=속성의 값
for a in list:
    #href = a.attrs["href"]
    href=a.get("href")
    print(href)

