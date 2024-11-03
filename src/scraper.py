import re
import requests
from bs4 import BeautifulSoup, Tag
from database import *
from time import sleep
from plugins.send import newItem

def getItemsFromUrl(url):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    try:
        pageGet = requests.get(url,headers=HEADERS)
    except Exception as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(pageGet.text, "html.parser")
    product_list_items = soup.find_all("div", class_=re.compile(r"item-card"))

    items = []

    for product in product_list_items:

        item= Item()
        item.title = product.find("h2").string
        try:
            price = product.find("p", class_=re.compile(r"price")).contents[0]
            # check if the span tag exists
            price_soup = BeautifulSoup(price, "html.parser")
            if type(price_soup) == Tag:
                continue
            # at the moment (20.5.2021) the price is under the 'p' tag with 'span' inside if shipping available
            price = int(price.replace(".", "")[:-2])
            item.price = price
        except:
            price = "Unknown price"
            item.price = None
        item.url = product.find("a").get("href")
        # page['sold'] = product.find("span", re.compile(r"item-sold-badge"))
        try:
            item.location = (
                product.find("span", re.compile(r"town")).string
                + product.find("span", re.compile(r"city")).string
            )
        except:
            item.location = "Unknown location"
        items.append(item)
    return items


async def scrape():
    while True:
        queries = getQueries()
        for query in queries:
            new=False
            items = getItemsFromUrl(query.url)
            for item in items:
                item.queryId = query.id
                # print(f"Title: {item.title}, price: {item.price}, url: {item.url}, location: {item.location}")
                if query.minPrice and item.price < query.minPrice:
                    continue
                if query.maxPrice and item.price > query.maxPrice:
                    continue
                if not isPresent(item):
                    print(f"New item found: {item.title}")
                    await newItem(item)
                    addItem(item)
                    new=True
            if not new:
                print(f"No new items found for query: {query.name}")
        sleep(60)

if __name__ == "__main__":
    url = "https://www.subito.it/annunci-lazio/vendita/usato/?q=macbook"
    for a in getItemsFromUrl(url):
        print(f"Title: {a.title}, price: {a.price}, url: {a.url}, location: {a.location}")