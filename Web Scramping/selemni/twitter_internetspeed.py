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
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
op.add_argument("start-maximized")


class speed_twitter_bot:
    def __init__(self):
        self.browser = webdriver.Chrome(service=service, options=op)
        self.up = 0
        self.down = 0

    def get_speed(self):
        self.browser.get(url="https://www.speedtest.net/")
        time.sleep(3)
        self.browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(40)
        self.up = self.browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = self.browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(self.up.text)
        print(self.down.text)
    def tweet(self):
        self.browser.get(url="https://twitter.com/i/flow/login")
        time.sleep(2)
        username = self.browser.find_element(By.NAME, "text")
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(1)
        password = self.browser.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        content = f"my upload speed is {self.up}, downlaod speed is {self.down}"
        write = self.browser.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        write.click()
        write.send_keys(content)

        self.browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click()
bot = speed_twitter_bot()
bot.get_speed()
bot.tweet()
