import re
import requests

if __name__ == "__main__":
    matches = set()
    with open("source_urls.txt") as inputs:
        for url in inputs:
            response = requests.get(url)
            for match in re.findall(
                    r"https:[a-zA-Z-_\/]*theonlinesweetshop\.com\/product[a-zA-Z-_\/]*\/", response.text):
                matches.add(match)

    with open("urls.txt", "w") as out:
        pass
    with open("urls.txt", "a") as out:
        for match in matches:
            out.write(match+"\n")
