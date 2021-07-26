# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:23:45 2021

@author: Nur Khadijah Safiy 
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

my_url = 'https://www.mudah.my/kuala-lumpur/for-sale?q=rumah%20untuk%20dijual'

hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(my_url,headers=hdr)
page = urlopen(req)
page_soup = BeautifulSoup(page.read(), "html.parser")

containers = page_soup.findAll("div",{"class":"sc-gwVKww cofoil"})

filename = "House Price Data.csv"
f = open(filename, "w")
headers = "Category, Price, Size, Bedrooms, Bathrooms \n"
f.write(headers)



for container in containers:
    
    catcontainer = container.findAll("div",{"class": "sc-esOvli zxCkq"})
    category = catcontainer[0].text
    price_container = container.findAll("div",{"class":"sc-bsbRJL iDlyvB"})
    priceK = price_container[0].text.strip()
    sizecontainer = container.findAll("div",{"class": "sc-esOvli zxCkq"})
    size = sizecontainer[1].text
    bedcontainer = container.findAll("div",{"class": "sc-esOvli zxCkq"})
    bed = bedcontainer[2].text
    bathcontainer = container.findAll("div",{"class": "sc-esOvli zxCkq"})
    bath = bathcontainer[3].text
    
    print("Category: " + category)
    print("Price: "+priceK)
    print("Size: " + size)
    print("Bedrooms: " + bed)
    print("Bathrooms: " + bath)
    
    f.write(category.replace(",",".") + priceK.replace(",",".")+  size.replace(",",".") + bed.replace(",",".") + bath.replace(",",".") + "\n")
	
f.close()
