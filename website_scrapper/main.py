import pandas
from bs4 import BeautifulSoup
import requests
from pandas import DataFrame

response = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(response, "html.parser")

story_links = soup.select(selector=".titlelink")
story_scores = soup.findAll(name="span", class_="score")

scrapped_data = {"article_names": [], "article_links": []}
for story_link in story_links:
    story_url = story_link.get("href")
    story_text = story_link.getText()
    scrapped_data["article_names"].append(story_text)
    scrapped_data["article_links"].append(story_url)

scrapped_df = pandas.DataFrame(scrapped_data)
scrapped_df.to_csv("scrapped_data.csv")
