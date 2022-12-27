import os
import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.instagram.com/"

ACCOUNT = "natgeo"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)
time.sleep(2)
browser.find_element(By.NAME, 'username').send_keys(USERNAME)
browser.find_element(By.NAME, 'password').send_keys(PASSWORD)
browser.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="mount_0_0_0+"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button').click()