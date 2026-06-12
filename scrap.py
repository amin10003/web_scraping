import requests
from bs4 import BeautifulSoup
import pandas as pd

show_scraped_data = []

def get_quote():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    # print(quotes)
    for qoute in quotes:
        motivation = qoute.span.text
        auther = qoute.small.text

        # print(f"Motivation: {motivation}\nAuther: {auther}")
        
        quot_dic = {
            "Author": auther,
            "Qoute": motivation
        }
        show_scraped_data.append(quot_dic)
        df = pd.DataFrame(show_scraped_data)
        df["Qoute"] = df["Qoute"].str.replace('""', ' ')
        print(df)


get_quote()






