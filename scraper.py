from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    print(quote.text + " ~ " + author.text)

# Video by tinkernut
