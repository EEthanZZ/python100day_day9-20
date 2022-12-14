import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "http://orteil.dashnet.org/experiments/cookie/"
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome = "C:/chromedriver_win32/chromedriver"
service = Service(chrome)
browser = webdriver.Chrome(service=service, options=op)
browser.get(url)

button = browser.find_element(By.ID, "cookie")

timeout = time.time() + 10
five_min = time.time() + 30

while True:
    button.click()

    if time.time() > timeout:
        money = int(browser.find_element(By.ID, "money").text.replace(",", ""))

        store = browser.find_elements(By.CSS_SELECTOR, "#store b")
        for upgrade in store[::-1]:
            upgrade_text = upgrade.text
            if upgrade_text != "":
                upgrades = upgrade_text.split("-")
                product = upgrades[0].strip()
                price = int(upgrades[1].strip().replace(",", ""))
                if money > price:
                    try:
                        browser.find_element(By.ID, f"Buy{product}").click()
                    except selenium.common.exceptions.NoSuchElementException:
                        continue

        timeout = time.time() + 10

    if time.time() > five_min:
        save = browser.find_element(By.ID, "exportSave")
        save.click()