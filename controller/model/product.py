import pandas as pd
import requests
from bs4 import BeautifulSoup

class Produto:

    def __init__(self, item_buscado):
        self.item_buscado = item_buscado
        self.url = 'https://lista.mercadolivre.com.br/' #Tô colocando o mercado livre como url padrão
        self.response = None
        self.content = None
        self.ofertas = None
        self.dataframe = None

    def get_response(self):
        self.response = requests.get(self.url+self.item_buscado)
        return self.response

    def get_content(self):
        self.content = self.response.content
        return self.content

    def get_offers(self):
        NameList = []
        mercadoLivre = BeautifulSoup(self.content, 'html.parser')#aqui ta o erro ó
        offers = mercadoLivre.find_all(
        'div', attrs={'class': 'ui-search-result__wrapper'})
        for offer in offers:
            links = offer.find('a', attrs={'class': 'ui-search-link'})
            price = offer.find('span', attrs={'class': 'price-tag-amount'})
            name = offer.find('h2', attrs={'ui-search-item__title'})
            discount = offer.find(
                'span', attrs={'ui-search-price__second-line__label'})
         
            if (discount): 
                NameList.append([name.text, price.text,discount.text,links['href']])
        self.ofertas = NameList
        return self.ofertas

    def get_dataframe(self):
        self.dataframe = pd.DataFrame(data=self.ofertas, columns=['name', 'price','discount', 'links'])
        return self.dataframe