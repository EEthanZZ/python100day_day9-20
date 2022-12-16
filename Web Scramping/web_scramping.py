import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/2022-12-12/"
# year = input("what year you would like to travel to? YYYY-MM-DD")
CLIENTID = "07911466c3be419680d2361b05020d0b"
CLIENT_SECRET = "34ac2e56b28b4fb4ba7eb69f487b122e"
REDIRECT_URI = "http://example.com/"

response = requests.get(url=URL)
web = response.text
soup = BeautifulSoup(web, 'html.parser')

musics = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
music_titles = [music.getText().strip("\n\t") for music in musics]
print(music_titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENTID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
user_id = sp.current_user()["id"]
print(user_id)