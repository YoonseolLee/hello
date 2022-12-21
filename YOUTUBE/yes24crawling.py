#https://www.youtube.com/watch?v=IGZcYh6l1Bo&ab_channel=%EC%98%A4%ED%86%A0%EC%BD%94%EB%8D%94
#예스24 베스트셀러 엑셀로 추출
#첫번째 strong 태그가 순위
#두번째 strong 태그가 제목
#마지막 em태그가 저자
#a태그에 href속성을 이용하면 url이 찍힘

import requests
from bs4 import BeautifulSoup

url = "http://www.yes24.com/Main/default.aspx"
res = requests.get(url)
#response 200이 떴다는 것은 테스트상 정상적으로 반환을 했다는 것을 의미
print(res)
#크롤링 할때 텍스트기반으로 파싱하기위해 res를 text로 파싱한 것
soup = BeautifulSoup(res.text, 'html.parser')
#li태그안에 tp02인걸 다 찾아내라
books = soup.select('li.tp02')

#엑셀로 추출(마지막 단계)
book_list = []

for book in books:
    rank = book.select('strong')[0].text #첫번째 strong은 순위이고, 두번째 strong은 제목이기 때문에 위치기반으로 인덱스로 처리
    title = book.select('strong')[1].text
    author = book.select('em')[1].text #두번째 em태그
    url = 'http://www.yes24.com' + book.select_one('a')['href'] #a태그가 하나이기 때문에 select_one을 써줘야함. select는 복수용이다. 
    book_list.append([rank,title,author,url])

import pandas as pd
df = pd.DataFrame(book_list, columns=['순위','제목','저자','링크'])
#index=False 의미: 데이터프레임을 저장할 때 인덱스가 기본으로 붙는데, 0부터 붙는다. 근데 랭크는 1부터 들어오기 때문에 헷갈릴 수 있으므로 안보이게 설정한 것.
df.to_excel('C:\Program Files\cs\PYTHON ETC\EXAMPLES\YOUTUBE\yes24_bestTop10.xlsx', index=False)