from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.com/dp/B0053WRWX8/ref=sbl_dpx_kitchen-electric-cookware_B09F6XHB4C_0?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
BUY_PRICE = 250



response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-price-whole", name="span").getText()
price_whole = int(price[:-1])
print(price_whole)

product = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText()
product_buy = product.strip()
print(product_buy)

if price_whole < BUY_PRICE:
    message = f"the {product_buy} is ${price_whole} now"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        result = connection.login("yczhu@yahoo.com", "email_password")
        connection.sendmail(
            from_addr="sendemail",
            to_addrs="gmail",
            msg=message
        )