#coding: utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup
#trazer a página inteira
html = urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.p.strong.getText())
