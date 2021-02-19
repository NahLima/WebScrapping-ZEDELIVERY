from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import csv

csvFileName = 'ZeDeliveryCidadesAtendidas.csv'

try:
    url = urlopen("https://www.ze.delivery/cidades-atendidas")
except HTTPError as error:
    print(error)
except URLError as error:
    print(error)
else:
    html = BeautifulSoup(url.read(),"html.parser")
    contentCities = html.find_all("li", {"class": "css-75eurm-citiesListCityName"})
    contentProvince = html.find_all("li", {"class": "css-162loec-provinceListItem"})
    
  
    with open(csvFileName, 'w') as csvfile:
        fileWriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        fileWriter.writerow(['ESTADO', 'CIDADE']) #HEADER 

        for cty, cr in zip(contentCities,contentProvince):        
            nameProvince = (cty.a).text
            nameCitie = (cty.a).text
            
            fileWriter.writerow([nameProvince, nameCitie]) #CONTENT
            print(nameProvince, nameCitie)
            
        print('Arquivo ', csvFileName, 'gerado com sucesso!')



        