import requests
from bs4 import BeautifulSoup

def spooder(max_pages):
    page = 1
    while page == max_pages:
        url = "https://osu.ppy.sh/p/beatmaplist?l=1&r=0&q=&g=0&la=0&ra=&s=4&o=1&m=-1&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a", {"class": "title"}):
            href = "https://osu.ppy.sh" + link.get("href")
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll("div", {"class": "beatmapListing"}):
        print(item_name.string)
        for link in soup.findAll('item_name.string'):
            href = "https://osu.ppy.sh" + link.get('href')
            print(href)



spooder(1)

