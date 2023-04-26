import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.imdb.com/chart/toptv/"

response = requests.get(URL)
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, 'html.parser')

tv_shows = soup.find_all(class_='lister-list')
# print(tv_shows)

title = [show.getText() for show in soup.select('td.titleColumn a')]
cast = [show.get('title') for show in soup.select('td.titleColumn a')]
ratings = [rating.getText() for rating in soup.select('td.imdbRating strong')]
year = [year.getText() for year in soup.select('td.titleColumn span')]
votes = [vote.get('title')[13:19].replace(',', '') for vote in soup.select('td.imdbRating strong')]


dataframe = pd.DataFrame(
    {"Title": title,
     "Cast": cast,
     "Year": year,
     "Ratings": ratings,
     "Votes": votes,
     })

dataframe.to_csv('tv_shows.csv')
