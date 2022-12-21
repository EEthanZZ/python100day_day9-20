import os
import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://tinder.com/"

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)

browser.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()