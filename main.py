from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

user_date_choice = input("What time period of songs do you want to go back to? Specify with format YYYY-MM-DD: ")

TOP_100_MUSIC_API_ENDPOINT = f"https://www.billboard.com/charts/hot-100/{user_date_choice}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=TOP_100_MUSIC_API_ENDPOINT, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_titles = soup.select("div ul li ul li h3#title-of-a-story") 
list_of_song_names = []
list_of_song_names = [song_name.get_text(strip=True) for song_name in song_titles]

# print(list_of_song_names)

# authenticating to spotify using spotipy 
spotipy_scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"), # the sp varibale is our API key
                                               client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
                                               scope=spotipy_scope))

user_info = sp.current_user()  # Get user details
user_id = user_info["id"]  # Extract the user ID
# playlist_add_items(playlist_id, items, position=None)
spotify_song_uri = []


# TODO Figure out all of the URIs of each song

# print(list_of_song_names[1])
# print(sp.search(q=list_of_song_names[1], type="track"))

song_uris = []
for song in list_of_song_names:
    result = sp.search(q=song, type="track", limit=1)  # Search for the song
    try:
        uri = result["tracks"]["items"][0]["uri"]  # Extract the URI
        song_uris.append(uri)
    except:
        print(f"{song} cannot be found on spodify")
print(len(song_uris))



# TODO Make the paylist 

# TODO Add every track to the playlist

