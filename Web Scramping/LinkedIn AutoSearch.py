import os
import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
url = "https://www.linkedin.com/jobs/search/?currentJobId=3162045938&distance=25&f_AL=true&geoId=100992797&keywords=information%20technology%20support%20technician&location=Melbourne%2C%20Victoria%2C%20Australia&refresh=true&sortBy=R"
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)

time.sleep(2)
sign_in = browser.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

user = browser.find_element(By.ID, "username")
user.send_keys(USERNAME)
password = browser.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

browser.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card").click()
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3162045938-4856673786530167398-phoneNumber-nationalNumber"]').send_keys("404346835")

