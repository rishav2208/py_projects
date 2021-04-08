from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")

content=response.text

soup=BeautifulSoup(content, "html.parser")

rank=soup.find_all(name="h3", class_="title")

movies=[movie.getText() for movie in rank]
movies=movies[::-1]

with open("movies.txt", mode="w") as f:
    for m in movies:
        f.write(f"{m}\n")
