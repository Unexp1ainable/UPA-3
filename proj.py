import re
from os import walk

if __name__ == "__main__":
    matches = set()
    for path in list(walk("htmls/"))[0][2]:
        with open(f"htmls/{path}") as file:
            for match in re.findall(r"https:[a-zA-Z-_\/]*theonlinesweetshop\.com\/product[a-zA-Z-_\/]*\/", file.read()):
                matches.add(match)

    with open("products-urls.txt", "w") as out:
        pass
    with open("products-urls.txt", "a") as out:
        for match in matches:
            out.write(match+"\n")
