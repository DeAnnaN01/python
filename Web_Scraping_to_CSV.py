### Web_Scraping_to_CSV 
### Written for learning by DeAnna
### 7-27-2022

from cgi import print_arguments
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

## Site to scrape
my_url="https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

## See how many html containers are present in this link.
containers = page_soup.findAll("div", {"class": "_3O0U0u"})
print(len(containers))

print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img["alt"])

