
#예스24 베스트셀러 엑셀로 추출
#첫번째 strong 태그가 순위
#두번째 strong 태그가 제목
#마지막 em태그가 저자
#a태그에 href속성을 이용하면 url이 찍힘

import requests
from bs4 import BeautifulSoup

url = "http://www.yes24.com/Main/default.aspx"
res = requests.get(url)
print(res)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select('li.tp02')

book_list = []

for book in books: 
    rank = book.select('strong')[0].text
    title = book.select('strong')[1].text
    author = book.select('em')[1].text
    url = 'http://www.yes24.com' + book.select_one('a')['href']
    book_list.append([rank,title,author,url])

import pandas as pd
df = pd.DataFrame(book_list, columns=['순위','제목','저자','링크'])
df.to_excel('C:\Program Files\cs\PYTHON ETC\EXAMPLES\YOUTUBE\yes24_bestTop10.xlsx', index=False)

