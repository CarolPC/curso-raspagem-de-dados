#coding: utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento")
bsObj = BeautifulSoup(html, "xml")
gastos = bsObj.findAll("valorTotalPrevisto")

soma = 0
for gasto in gastos:
    soma = soma + (float(gasto.get_text()))
print(soma)
