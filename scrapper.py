import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = ("https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=&zip=54001")

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

res = page_soup.find_all("div", {"class": "gKx_hQ Dk8CJT"})

print(len(res))
