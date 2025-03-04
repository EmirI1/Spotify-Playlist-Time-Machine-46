from bs4 import BeautifulSoup
import requests

user_date_choice = input("What time period of songs do you want to go back to? Specify with format YYYY-MM-DD: ")

API_ENDPOINT = f"https://www.billboard.com/charts/hot-100/{user_date_choice}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=API_ENDPOINT, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_titles = soup.select("div ul li ul li h3#title-of-a-story") 
list_of_song_names = []
for song_name in song_titles:
    list_of_song_names.append(song_name.get_text(strip=True))



