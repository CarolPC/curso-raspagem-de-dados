#coding: utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.dicionariodenomesproprios.com.br/top-brasil/")
bsObj = BeautifulSoup(html, "html.parser")

for item in range(0, 2):
    for nome in bsObj.findAll("ol",  {'class':"top-list"})[item]:
        print(nome.a.get_text())
