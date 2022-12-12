from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web = response.text
soup = BeautifulSoup(yc_web, "html.parser")


links = soup.find_all(class_="titleline")
article_links = [link_tag.find(name="a").get("href") for link_tag in links]
article_titles = [link_title.getText() for link_title in links]
print(article_titles)
print(article_links)
artical_upvotes = soup.find_all(name="span", class_="score")
votes = [i.getText().split()[0] for i in artical_upvotes]
print(votes)

# with open("website.html", encoding="utf8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# a = soup.title
# print(a)
# print(a.name)
# print(a.string)
#
# all_anchor_tag = soup.find_all(name="a")
# for tag in all_anchor_tag:
#     print(f"{tag.getText()}: {tag.get('href')}")
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# sec_heading = soup.find(name="h3", class_="heading")
# print(sec_heading)
#
# company_url = soup.select(selector=".heading")
# print(company_url)