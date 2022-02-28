import requests
from bs4 import BeautifulSoup

from datetime import datetime



headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
page = requests.get("https://br.investing.com/crypto/bitcoin/btc-brl", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
respostas = soup.find_all("span", class_="text-2xl")
def dataHora():
    data = datetime.now().strftime('%d-%m-%Y %H:%M')
    print("Data e hora:",data)

print("Valor do Bitcoin atualizado: R$",respostas[0].text)
dataHora()

