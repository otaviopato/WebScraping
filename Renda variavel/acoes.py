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
bitcoin = requests.get("https://br.investing.com/crypto/bitcoin/btc-brl", headers=headers)
petroleo = requests.get("https://br.financas.yahoo.com/quote/CL%3DF?p=CL%3DF", headers=headers)
gol = requests.get("https://br.investing.com/equities/gol-pn-es-n2", headers=headers)
viaVarejo = requests.get("https://br.investing.com/equities/via-varejo-sa", headers=headers)
petrobras = requests.get("https://br.investing.com/equities/petrobras-pn", headers=headers)
magalu = requests.get("https://br.investing.com/equities/magaz-luiza-on-nm", headers=headers)
btgPactual = requests.get("https://br.investing.com/equities/bb-renda-corporativa", headers=headers)
with open ('acoes.txt','a',newline='', encoding='utf-8') as f:
#Variables to access the body of the site
    soupIbovespa = BeautifulSoup(ibovespa.content, 'html.parser')
    soupDolar = BeautifulSoup(dolar.content,'html.parser')
    soupBitcoin = BeautifulSoup(bitcoin.content, 'html.parser')
    soupPetroleo = BeautifulSoup(petroleo.content, 'html.parser')
    soupViaVarejo = BeautifulSoup(viaVarejo.content, 'html.parser')
    soupGol = BeautifulSoup(gol.content, 'html.parser')
    soupPetrobras = BeautifulSoup(petrobras.content, 'html.parser')
    soupMagalu = BeautifulSoup(magalu.content, 'html.parser')
    soupBtgPactual = BeautifulSoup(btgPactual.content, 'html.parser')
    #Date and time function
    date = datetime.now().strftime('%d-%m-%Y %H:%M')
    data = ("Data e hora da consulta: " + date)
    #Search class to collect data from websites
    resIbovespa = soupIbovespa.find_all("span", class_="text-2xl")
    resDolar = soupDolar.find_all("span", class_="DFlfde SwHCTb")
    resBitcoin = soupBitcoin.find_all("span", class_="text-2xl")
    resPetroleo = soupPetroleo.find_all("fin-streamer",class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
    resGol = soupGol.find_all("span", class_="text-2xl")
    resViaVarejo = soupViaVarejo.find_all("span", class_="text-2xl")
    resPetrobras = soupPetrobras.find_all("span", class_="text-2xl")
    resMagalu = soupMagalu.find_all("span", class_="text-2xl")
    resBtgPactual = soupBtgPactual.find_all("span", class_="text-2xl")
    end = time.time()
    result = ("\nRENDA VARIÁVEL \n" + data + "\n-------------------- \nIBOVESPA " + resIbovespa[0].text + "\nDOLAR R$" + resDolar[0].text + "\nBITCOIN R$" + resBitcoin[0].text + "\nPETRÓLEO R$" + resPetroleo[0].text + "\nGOLL4 R$" + resGol[0].text + "\nVIIA3 R$" + resViaVarejo[0].text + "\nPETR4 R$" + resPetrobras[0].text + "\nBCFF11 R$" + resBtgPactual[0].text + "\nMGLU3 R$" + resMagalu[0].text + "\n--------------------" + "\n")
    #runtime analysis
    print(result)
    print("Tempo de execução",end - start,"\n--------------------")
    f.write(result)