import requests
from bs4 import BeautifulSoup

def add_plus(keywords):
    keywords = keywords.split()
    keyword_edited = ""
    for i in keywords:
        keyword_edited += i + "+"
    keyword_edited = keyword_edited[:-1]
    return keyword_edited

class EbayScraper:

    def __init__(self, keyword):
        self.keyword = keyword
        plusified_keyword = add_plus(keyword)
        self.products = []
        self.search_url = "https://www.ebay.com/sch/i.html?_nkw=" + plusified_keyword

    def scrape_products(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 
(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        content = requests.get(self.search_url, headers=headers).text
        soup = BeautifulSoup(content, "html.parser")
        product_list = []
        products = soup.find("ul", {"class": "srp-results srp-list 
clearfix"}).find_all("li", {"class": "s-item    s-item--watch-at-corner"})
        for product in products:
            div = product.find("div", {"class": "s-item__info clearfix"})
            name = div.find_all("a")[0].text
            price = div.find('span', {"class": "s-item__price"}).text
            product_list.append({
                "name": name,
                "price": price
            })
        return product_list

x = EbayScraper("hisense tv")
x.scrape_products()