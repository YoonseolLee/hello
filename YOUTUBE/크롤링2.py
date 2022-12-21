#https://www.youtube.com/watch?v=aYwg1H5BK04&ab_channel=%EA%B8%B0%EC%88%A0%EB%85%B8%ED%8A%B8with%EC%95%8C%EB%A0%89
#파이썬 웹 크롤링 하기 - 너무 간단해서 민망합니다

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://sports.news.naver.com/kbaseball/index")

bsObject = BeautifulSoup(html, "html.parser")  #html의 내용을 받은 다음, 이 html에 대해 접근 할 수 있게 해주는 함수임.

# BeautifulSoup 객체는 웹문서를 파싱한 상태
#     파싱 :  일련의 문자열로 구성된 문서를 의미 있는 토큰(token)으로 분해하고  
#             토큰으로 구성된 파스 트리(parse tree)를 만드는 것
# 웹 문서가 태그 별로 분해되어 태그로 구성된 트리가 구성

#이 사이트의 기사(링크)를 다 가져옴
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))

