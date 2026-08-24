import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)

print(response.status_code)


soup = BeautifulSoup(response.text, "html.parser")


quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)


authors = soup.find_all("small", class_="author")

for author in authors:
    print(author.text)


for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print(text)
    print(author)
    print()