import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET_KEY"]
URI_REDIRECT = "http://localhost:8888/callback"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                       client_id=SPOTIFY_CLIENT_ID,
                       client_secret=SPOTIFY_CLIENT_SECRET,
                       redirect_uri=URI_REDIRECT,
                       cache_path="token.txt",
                       scope="playlist-modify-private",
                       show_dialog=True))

user_id = sp.current_user()["id"]
# print(user_id)

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
SPOTIFY_URL = f"https://www.billboard.com/charts/hot-100/{date}/"

# Scraping Billboard 100
response = requests.get(SPOTIFY_URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
titles = soup.find_all(name="h3", class_="u-letter-spacing-0021")
all_songs = [title.getText().strip() for title in titles]

top_titles = []
for song in all_songs:
    if song != "Songwriter(s):" and song != "Imprint/Promotion Label:" and song != "Producer(s):":
        top_titles.append(song)
# print(top_titles)

# Searching spotify for songs by title
song_uris = []
year = date.split("-")[0]
for title in top_titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

# Creating new private playlist in Spotify
playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

# Adding songs found into the new playlist
songs_added = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(songs_added)
