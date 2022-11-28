#/usr/bin/bash
python3 get_urls.py > product_urls.txt
python3 get_price.py < product_urls.txt