from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/"
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)

first_name = browser.find_element(By.NAME, "fName")
first_name.send_keys("Ethan")
last_name = browser.find_element(By.NAME, "lName")
last_name.send_keys("Z")
email = browser.find_element(By.NAME, "email")
email.send_keys("aa@yahoo.com")