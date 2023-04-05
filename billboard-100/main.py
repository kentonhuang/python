from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("C:/Users/huang/PycharmProjects/EnvironmentVariables/.env")

scope = "playlist-modify-private"

client_id = os.getenv("SPOTIFY_CLIENT_ID")
secret_id = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri="http://example.com/", client_id=client_id, client_secret=secret_id,show_dialog=True, cache_path="Token.txt"))
user_id = sp.current_user()["id"]

date = input("What year do you want to travel to? TYpe the date in this format YYYY-MM-DD:")

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_url)

soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")
song_titles = [title.getText().strip("\n\t") for title in songs]
artists = soup.find_all(name="span", class_="u-max-width-330")
artist_names = [name.getText().strip("\n\t") for name in artists]
song_and_artist = dict(zip(song_titles, artist_names))

song_uris = []

for(song, artist) in song_and_artist.items():
    try:
        result = sp.search(q=f"track:{song} artist:{artist}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        pass

print(f"Number of songs found: {len(song_uris)}")
print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, )
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)