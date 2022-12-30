import os
import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
url = "https://www.instagram.com/"

ACCOUNT = "natgeo"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
op.add_argument("start-maximized")


class iG_follower:
    def __init__(self):
        self.browser = webdriver.Chrome(service=service, options=op)

    def login(self):
        self.browser.get(url)
        time.sleep(2)
        self.browser.find_element(By.NAME, 'username').send_keys(USERNAME)
        self.browser.find_element(By.NAME, 'password').send_keys(PASSWORD)
        self.browser.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
        time.sleep(4)
        try:
            self.browser.find_element(By.XPATH,
                                      '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button').click()
            time.sleep(2)
            self.browser.find_element(By.XPATH,
                                      '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()
        except:
            self.browser.find_element(By.XPATH,
                                      '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()
        time.sleep(2)

    def find_followers(self):
        self.browser.get(url=f"{url}/{ACCOUNT}")
        time.sleep(4)
        self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div['
                                            '1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(5)
        # select the scrollable part of the popup window
        pop_up_window = self.browser.find_element(By.CSS_SELECTOR, '._ab8w ._aano')
        # scroll down to load more and more followers
        for i in range(100):
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up_window)
        time.sleep(2)

    def follow(self):
        followers_list = self.browser.find_elements(By.CSS_SELECTOR, '.PZuss li button')
        # loop through each follower in follower list
        for follower in followers_list:
            try:
                follower.click()
                time.sleep(1)
            # if sometimes we click on following instead of follow, so instagram displays pop up to confirm unfollow
            except ElementClickInterceptedException:
                # click on cancel
                self.browser.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]').click()
                time.sleep(2)



bot = iG_follower()
bot.login()
bot.find_followers()
bot.follow()
