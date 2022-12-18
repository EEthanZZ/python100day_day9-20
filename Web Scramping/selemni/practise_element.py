from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://www.python.org/"
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)

date = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")

event = browser.find_elements(By.CSS_SELECTOR, ".event-widget li a")

