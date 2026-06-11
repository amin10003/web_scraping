import requests
from bs4 import BeautifulSoup


def get_quote():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    # print(quotes)
    for qoute in quotes:
        motivation = qoute.span.text
        auther = qoute.small.text

        print(f"Motivation: {motivation}\nAuther: {auther}")


get_quote()
