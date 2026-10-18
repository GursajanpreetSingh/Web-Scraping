import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content,"html.parser")

movies = [movie.get_text().strip() for movie in soup.find_all(name="h3",class_="title")]
# movies = [movie.get_text().split(")")[-1].strip() for movie in soup.find_all(name="h3",class_="title")]
movies = movies[::-1]

with open("movies.txt","w",encoding="utf-8") as file:
    for movie in movies:
        file.write(movie+"\n")

