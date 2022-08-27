### Web_Scraping_to_CSV 
### Written for learning by DeAnna
### 7-27-2022

from cgi import print_arguments
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

## Site to scrape
my_url="https://www.flipkart.com/mobiles/samsung~brand/pr?sid=tyy,4io"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

## See how many html containers are present in this link.
containers = page_soup.findAll("div", {"class": "_3O0U0u"})
print(vars(containers))

print(len(containers))
container = list[containers[0]]


print(soup.prettify(containers[0]))

container = list[containers[0]]
print(container.div.img["alt"])

