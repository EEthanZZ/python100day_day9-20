from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
a = soup.title
print(a)
print(a.name)
print(a.string)

all_anchor_tag = soup.find_all(name="a")
for tag in all_anchor_tag:
    print(f"{tag.getText()}: {tag.get('href')}")