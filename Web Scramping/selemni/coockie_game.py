from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "http://orteil.dashnet.org/experiments/cookie/"
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)


button = browser.find_element(By.ID, "cookie")

store = browser.find_element(By.ID, "store")
while True:
    button.click()

