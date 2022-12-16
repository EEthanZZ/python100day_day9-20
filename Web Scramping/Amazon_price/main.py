from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://www.amazon.com/dp/B0053WRWX8/ref=sbl_dpx_kitchen-electric-cookware_B09F6XHB4C_0?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())