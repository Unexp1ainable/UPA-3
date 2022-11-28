from bs4 import BeautifulSoup
import requests
from sys import stdin 

def get_price(url: str):
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    titles = soup.find_all("h1", {"class": "product-title"})
    title = titles[0]
    
    price_divs = soup.find_all("div", {"class": "price-wrapper"})
    price_div = price_divs[0]
    
    print(url + "\t" + title.text.strip() + "\t" + price_div.p.text.strip())


if __name__ == "__main__":
    for line in stdin:
        get_price(line[:-1])