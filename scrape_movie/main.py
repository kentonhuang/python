import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.encoding = "utf-8"
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")][::-1]

with open("movies.txt", "a") as file:
    for movie in movies:
        file.write(f"{movie}\n")



