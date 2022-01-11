import requests
from bs4 import BeautifulSoup
import pandas as pd

# Getting the website HTML
website_template = requests.get("https://www.imdb.com/search/title/?groups"
                                "=top_100&sort=user_rating,desc").text
# Creating a Beautiful Soup instance to get access to the HTML content (being
# able to query elements)
soup = BeautifulSoup(website_template, "html.parser")
scrapped_data_dict = {"Rank": [], "Movie name": [], "Date of release": []}
# Getting all the movies names (inspect the page in your browser to find out
# how you can isolate the relevant components)

# getting the names of the movies
movie_names = soup.select(selector=".lister-item-header a")

# getting the year of release
date_of_release = soup.select(selector=".lister-item-year")

# getting the rankings
rankings = soup.select(selector=".lister-item-index")

for index, value in enumerate(movie_names):
    movie_name = value.getText()
    movie_ranking = int(rankings[index].getText().split(".")[0])
    movie_date_of_release = date_of_release[index].getText()
    scrapped_data_dict["Rank"].append(movie_ranking)
    scrapped_data_dict["Movie name"].append(movie_name)
    scrapped_data_dict["Date of release"].append(movie_date_of_release)

df = pd.DataFrame(scrapped_data_dict)
df.to_csv("Top 50 movies.csv")
