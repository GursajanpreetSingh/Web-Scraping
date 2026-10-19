from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

scope = "playlist-modify-private"

date = input("Which year do you want to travel to? Type the dat in this format YYYY-MM-DD:")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/135.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=header)
content = response.text

soup = BeautifulSoup(content, "html.parser")

songs = [song.get_text().strip() for song in soup.select("li ul li h3")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]

for song in songs:
    result = sp.search(
        q=f"track:{song} year:{year}",
        type="track"
    )

    try:
        uri = result["tracks"]["items"][0]["uri"]
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped.")

print(songs)
print(song_uris)

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

print(playlist)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)