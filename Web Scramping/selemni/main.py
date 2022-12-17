from selenium import webdriver
from selenium.webdriver.chrome.service import Service

op = webdriver.ChromeOptions()
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get("https://www.google.com")
browser.close()

