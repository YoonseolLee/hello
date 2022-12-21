import requests
from bs4 import BeautifulSoup

req = requests.get("https://m.blog.naver.com/luvpolo/221300832833")
req.text
soup = BeautifulSoup(req.content, "html.parser")

span_list = soup.find("tbody").find_all("span")
for span in span_list:
    print(span.text) #.text는 텍스트화 시킨다. 

span_list2 = []
for span in span_list:
    span_list2.append(span.text)
print(span_list2)

del span_list2[0]
print(span_list2)