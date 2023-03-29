from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_links = []
article_texts = []

news = soup.find_all(class_="titleline")
for heading in news:
    article_links.append(heading.find(name="a").get("href"))
    article_texts.append(heading.find(name="a").getText())

# scores = soup.find_all(class_="score")
# for score in scores:
#     article_upvotes.append(score.getText().split(" ")[0])

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]

print(article_links)
print(article_texts)
print(article_upvotes)

max = 0
index = 0
for i in range(1, len(article_upvotes)):
    if article_upvotes[i] > max:
        max = article_upvotes[i]
        index = i

print(article_texts[index])
print(article_links[index])