import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/2022-12-12/"
# year = input("what year you would like to travel to? YYYY-MM-DD")

response = requests.get(url=URL)
web = response.text
soup = BeautifulSoup(web, 'html.parser')

musics = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
music_titles = [music.getText().strip("\n\t") for music in musics]
print(music_titles)
