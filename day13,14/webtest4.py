from bs4 import BeautifulSoup
html = """
    <html>
        <head>
            <title>파이썬 웹 크롤링</title>
        </head>
        <body>
            <h1 id="title" class="hello">안녕하세요</h1>
            <p id="name">정수아입니다</p>
        </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one("h1.hello")
print("title : " + title.string)
#clasee => .
#id => #