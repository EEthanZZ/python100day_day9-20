from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.timeout.com/newyork/movies/best-movies-of-all-time")
movies = response.text
soup = BeautifulSoup(movies, "html.parser")

movies_100 = soup.find_all(name="h3", class_="_h3_cuogz_1")
movies_name = [i.getText() for i in movies_100]
for i in movies_name:
    a = str("\xa0")
    if a in i:
        x = i.replace(a, "")
    print(x)

