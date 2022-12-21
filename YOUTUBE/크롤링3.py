from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("존시나")
elem.send_keys(Keys.RETURN)
driver.find_elements(By.CSS_SELECTOR, ".tQj5Y")[0].click()
time.sleep(3)
#터미널에서 devtools라는 글자 이후 주소가 src이다. 
imgUrl= driver.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute("src") 

#python download image by url // import urllib.request도 세트임.
urllib.request.urlretrieve(imgUrl, "test2.jpg")

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()