from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.ze.delivery/cidades-atendidas")

html = BeautifulSoup(url.read(),"html.parser")
contentCities = html.find_all("li", {"class": "css-75eurm-citiesListCityName"})

    
for cty in contentCities:        
    citiesName = (cty.a).text
   
    print(citiesName)

