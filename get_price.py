from bs4 import BeautifulSoup
import requests

def get_price(urls: list):
    for url in urls:
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.text, 'html.parser')

        titles = soup.find_all("h1", {"class": "product-title"})
        title = titles[0]
        
        price_divs = soup.find_all("div", {"class": "price-wrapper"})
        price_div = price_divs[0]
        
        print(url + "\t" + title.text.strip() + "\t" + price_div.p.text.strip())


if __name__ == "__main__":
    urls = [
        "https://theonlinesweetshop.com/product/strawberry-twist-kisses-party-sweets-bucket/",
        "https://theonlinesweetshop.com/product/melody-pops/",
        "https://theonlinesweetshop.com/product/candy-chocolate-footballs/",
        "https://theonlinesweetshop.com/product/strawberry-pencil-bites/",
    ]

    get_price(urls)