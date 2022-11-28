#/usr/bin/bash
python3 get_urls.py > urls.txt

head -20 urls.txt | 
while read URL; do
  python3 get_price.py URL; 
done