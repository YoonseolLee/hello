# https://www.youtube.com/watch?v=1b7pXC1-IbE&list=WL&index=1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
#F12에서 classname은 여러 개 중복 될 수 있음 따라서 더 구체적으로 하려면, 
#찾고자하는 태그에서 우클릭-copy-selector 또는 XPath 또는 fullXPath를 이용-fullxpath가 가장 구체적임
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q") #f12 눌러서 검색창에 해당하는 것 입력
elem.send_keys("조코딩") #검색창에 입력할 키워드
elem.send_keys(Keys.RETURN) #엔터

#이미지를 최대한 많이 받으려면 스크롤을 맨 밑까지 해야함. 
SCROLL_PAUSE_TIME = 1 #에러가 뜨면 로딩시간이 불충분 한거니까 충분히 잡기
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight") #자바스크립트로 스크롤의 높이를 last_height에 저장함
while True: #무한반복
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #브라우저 끝까지 스크롤을 내리겠다

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME) #1초동안 페이지가 로딩 될 때 까지 기다림

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight") #변화한 스크롤의 높이가 있다면 계속 반복
    if new_height == last_height: # 이전 스크롤이나 내린 스크롤이나 높이가 같으면
        try:
            driver.find_elements(By.CSS_SELECTOR, ".mye4qd").click() #결과더보기 버튼이 있으면 자동으로 클릭
        except:
            break #결과 더보기 버튼이 없으면 반복문 종료
            
    last_height = new_height #만약에 내렸을 때 뭐가 더 떠서 스크롤이 더 길어진다면 그때는 값이 이전보다 커짐

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd") 
count = 1
#class니까 . 찍은 것임 #css강좌 듣기 #클릭 = [0].click()은 가장 첫번째 요소를 끄집어내서 그것을 클릭하겠다는 뜻임
for image in images:
    try:
        image.click() #클릭
        time.sleep(3) #클릭,이동 할 때는 브라우저도 어느정도 시간이 필요함 따라서 시간을 지연시킨다.
        #큰 이미지의 주소 = f12해서 src 뒤에 있는 주소
        imgURL = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src") #full xpath/get attribute는, 사진의 src를 가져와서 다운로드 받으라는 것임
        urllib.request.urlretrieve(imgURL, str(count) + ".jpg") #탐색기->selenium폴더에 test.jpg가 다운받아짐
        count = count + 1 
    except:
        pass
    #사진 여러 개를 다운받을 것이니까 반복문을 사용한다. 

driver.close()

