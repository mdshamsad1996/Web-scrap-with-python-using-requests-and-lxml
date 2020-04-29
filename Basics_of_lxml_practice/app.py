from lxml import etree


import lxml.html
import requests, os
import urllib.request as urllib2
import pprint
import http.cookiejar as cookielib
import pytesseract
from PIL import Image, ImageOps
from io import BytesIO
from subprocess import check_output


tree = etree.parse("fundamentals/src/web_page.html")

print(etree.tostring(tree))
title_element = tree.xpath("//title/text()")[0]
print(title_element)
paragraph_element = tree.xpath("//p/text()")[0]
print(paragraph_element)

list_items = tree.xpath("//li")
for li in list_items:
    text = ''.join(map(str.strip,li.xpath(".//text()")))
    print(text)

# using cssselect 

html = tree.getroot()
print(html)

title_element = html.cssselect("title")[0]
print(title_element.text)

paragraph_element = html.cssselect("p")[0]
print(paragraph_element.text)

list_items = html.cssselect("li")
for li in list_items:
    a = li.cssselect('a')
    if len(a) ==0:
        print(li.text)
    else:
        print(f"{li.text.strip()} {a[0].text}")






    

