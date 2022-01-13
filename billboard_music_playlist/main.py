from bs4 import BeautifulSoup
import requests as http

html_page_content = http.get("https://www.billboard.com/charts/hot-100/2010"
                             "-08-07/").text
query_able_page = BeautifulSoup(html_page_content, "html.parser")

songs = query_able_page.select(selector="li h3#title-of-a-story")
songs_title = [song.getText() for song in songs]
