import os
import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "https://tinder.com/"

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)

browser.maximize_window()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]').click()

browser.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(1)

browser.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()
time.sleep(1)

main_window = browser.window_handles[0]
login_page = browser.window_handles[1]
browser.switch_to.window(login_page)

browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(USERNAME)
browser.find_element(By.XPATH, '//*[@id="pass"]').send_keys(PASSWORD)
browser.find_element(By.XPATH, '//*[@id="pass"]').send_keys(Keys.ENTER)
time.sleep(3)
# browser.maximize_window()
# time.sleep(2)
# browser.find_element(By.XPATH, '//*[@id="mount_0_0_5F"]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div').click()
# time.sleep(5)
# browser.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div[2]/div/input').send_keys("404346835")

browser.switch_to.window(main_window)
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[2]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[2]/div[2]').click()
time.sleep(8)
action = ActionChains(browser)
for i in range(0,100):
    action.send_keys(Keys.ARROW_RIGHT)
    action.perform()