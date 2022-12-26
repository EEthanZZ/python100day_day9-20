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


class speed_twitter_bot:
    def __init__(self):
        self.browser = webdriver.Chrome(service=service, options=op)
        self.up = 0
        self.down = 0

    def get_speed(self):
        pass

    def tweet(self):
        pass

