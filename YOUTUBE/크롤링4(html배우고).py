#https://webnautes.tistory.com/779
#https://jhnoru.tistory.com/20

from urllib.request import urlopen
from bs4 import BeautifulSoup

html  = urlopen("https://www.naver.com/")
bsObject = BeautifulSoup(html, "html.parser")

#head에 포함된 title(NAVER)을 확인함
print(bsObject.head.title)

#웹문서에서 메타데이터만 찾아서 content 속성값을 가져옴.
for meta in bsObject.head.find_all('meta'):
    print(meta.get('content')) 

#원하는 태그의 내용 가져오기
print (bsObject.head.find("meta", {"name":"description"}).get('content'))

#모든 링크의 텍스트와 주소를 가져오기
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
    
####### html 공부 후 다시 볼 것