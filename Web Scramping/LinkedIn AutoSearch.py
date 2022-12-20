import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://www.linkedin.com/jobs/search/?currentJobId=3162045938&distance=25&f_AL=true&geoId=100992797&keywords=information%20technology%20support%20technician&location=Melbourne%2C%20Victoria%2C%20Australia&refresh=true&sortBy=R"
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)