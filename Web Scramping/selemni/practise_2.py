from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://en.wikipedia.org/wiki/Main_Page"
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)

number = browser.find_element(By.CSS_SELECTOR, "#articlecount a")
print(number.text)

search = browser.find_element(By.NAME, "search")
search.send_keys("python")