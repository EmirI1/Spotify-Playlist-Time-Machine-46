from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_input = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
base_url = "https://www.billboard.com/charts/hot-100/"


response = requests.get(url=f"{base_url}{user_input}/", headers=header)
response.raise_for_status
html_webpage = response.text

soup = BeautifulSoup(html_webpage, "html.parser")
web_scraped_song_names = soup.select("li ul li h3")

lst_of_song_names = [song.getText().strip() for song in web_scraped_song_names]

# Using spotipy for authenticating to the user 

scope = "user-library-read"



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.current_user_saved_tracks()
print(results)