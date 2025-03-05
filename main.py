from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

user_date_choice = input("What time period of songs do you want to go back to? Specify with format YYYY-MM-DD: ")

API_ENDPOINT = f"https://www.billboard.com/charts/hot-100/{user_date_choice}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=API_ENDPOINT, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_titles = soup.select("div ul li ul li h3#title-of-a-story") 
list_of_song_names = []
list_of_song_names= [song_name.get_text(strip=True) for song_name in song_titles]

# authenticating to spotify using spotipy 
spotipy_scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"), # the sp varibale is our API key
                                               client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
                                               scope=spotipy_scope))



