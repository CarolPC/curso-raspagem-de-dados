#coding: utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.cinemark.com.br/")
bsObj = BeautifulSoup(html, "html.parser")

for movie in bsObj.findAll("h3",  {'class':"movie-title"}):
    if (movie.a.span):
        print(movie.a.span.get_text())
    else:
        print(movie.a.get_text())
