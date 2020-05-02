pip install beautifulsoup4
pip install lxml

from bs4 import BeautifulSoup
import requests
url = "http://servicos2.sjc.sp.gov.br/servicos/horario-e-itinerario.aspx?acao=p&opcao=1&txt="
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lista_itinerarios = soup.find_all('table', class_='textosm')
url = 'http://www.sjc.sp.gov.br'
for lista_td in lista_itinerarios:
    lista = lista_td.find_all('td')
    for lista_dados in lista:
        if lista_dados.next_element.name == 'a':
            url_it = '{0}{1}'. format (url, lista_dados.next_element.get('href'))
            print(url_it)
        else:
            print(lista_dados.next_element)