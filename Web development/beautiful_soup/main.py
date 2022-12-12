from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
a = soup.title
print(a)
print(a.name)
print(a.string)