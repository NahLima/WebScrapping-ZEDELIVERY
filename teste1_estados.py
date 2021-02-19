from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.ze.delivery/cidades-atendidas")

html = BeautifulSoup(url.read(),"html.parser")
contentProvince = html.find_all("li", {"class": "css-162loec-provinceListItem"})

    
for cty in contentProvince:        
    provinceName = (cty.a).text
   
    print(provinceName)

