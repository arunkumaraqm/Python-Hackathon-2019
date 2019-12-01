## B3) Scrap a flipkart.com for the book "The Alchemist" and get the rating and price of it.

## Please install bs4 and requests.

## Didn't really see the point of this problem.

from bs4 import BeautifulSoup
import requests 
url = "https://www.flipkart.com/alchemist/p/itmfc9jxsc7dckfm"
uclient = requests.get(url)
html_page = uclient.text
uclient.close()
soup = BeautifulSoup(html_page, "html.parser")
data = str(soup.findAll(class_ ="_1vC4OE _3qQ9m1"))
print("Price = ", data.lstrip('[<div class="_1vC4OE _3qQ9m1">').rstrip("</div>]"))
data = str(soup.findAll(class_ ="_1i0wk8"))
print("Rating = ", data.lstrip('[<div class="_1i0wk8">').rstrip("</div>]"))
