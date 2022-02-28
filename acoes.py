import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

start = time.time()

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
#Link to request the sites
ibovespa = requests.get("https://br.investing.com/indices/bovespa", headers=headers)
dolar = requests.get("https://www.google.com/search?q=dolar&rlz=1C1FCXM_pt-PTBR972BR972&oq=dolar&aqs=chrome.0.69i59j69i57j69i59l2j69i60j69i61j69i60l2.495j0j4&sourceid=chrome&ie=UTF-8", headers=headers)
gol = requests.get("https://br.investing.com/equities/gol-pn-es-n2", headers=headers)
viaVarejo = requests.get("https://br.investing.com/equities/via-varejo-sa", headers=headers)
petrobras = requests.get("https://br.investing.com/equities/petrobras-pn", headers=headers)
magalu = requests.get("https://br.investing.com/equities/magaz-luiza-on-nm", headers=headers)
btgPactual = requests.get("https://br.investing.com/equities/bb-renda-corporativa", headers=headers)

#Variables to access the body of the site
soupIbovespa = BeautifulSoup(ibovespa.content, 'html.parser')
soupDolar = BeautifulSoup(dolar.content,'html.parser')
soupViaVarejo = BeautifulSoup(viaVarejo.content, 'html.parser')
soupGol = BeautifulSoup(gol.content, 'html.parser')
soupPetrobras = BeautifulSoup(petrobras.content, 'html.parser')
soupMagalu = BeautifulSoup(magalu.content, 'html.parser')
soupBtgPactual = BeautifulSoup(btgPactual.content, 'html.parser')

#Date and time function
def dateHour():
    date = datetime.now().strftime('%d-%m-%Y %H:%M')
    print("Data e hora da consulta:",date)

#Search class to collect data from websites
resIbovespa = soupIbovespa.find_all("span", class_="text-2xl")
resDolar = soupDolar.find_all("span", class_="DFlfde SwHCTb")
resGol = soupGol.find_all("span", class_="text-2xl")
resViaVarejo = soupViaVarejo.find_all("span", class_="text-2xl")
resPetrobras = soupPetrobras.find_all("span", class_="text-2xl")
resMagalu = soupMagalu.find_all("span", class_="text-2xl")
resBtgPactual = soupBtgPactual.find_all("span", class_="text-2xl")

print("RENDA VARIÁVEL \n-------------------- \nIBOVESPA",resIbovespa[0].text,"\nDOLAR R$", resDolar[0].text, "\nGOLL4 R$",resGol[0].text,"\nVIIA3 R$",resViaVarejo[0].text,"\nPETR4 R$",resPetrobras[0].text, "\nBCFF11 R$",resBtgPactual[0].text,"\nMGLU3 R$",resMagalu[0].text,"\n--------------------")
dateHour()

#runtime analysis
end = time.time()
print("Tempo de execução",end - start,"\n--------------------")
