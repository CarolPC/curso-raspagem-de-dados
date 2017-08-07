#coding: utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup

for letter in range(65, 90):
    for item in range(1, 4):
        html = urlopen("https://www.bayerpet.com.br/Caes/lista-nomes/"+chr(letter)+"/"+str(item))
        bsObj = BeautifulSoup(html, "html.parser")
        for nome in bsObj.findAll("ul",  {'class':"list"}):
            print(nome.get_text())
