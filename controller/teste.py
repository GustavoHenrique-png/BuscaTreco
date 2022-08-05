from pandas.testing import assert_frame_equal
import pandas as pd
import requests
import unittest
from model.product import Produto
from app import app


class TestProduct(unittest.TestCase):

    #objeto que seta atributos necessários para o programa, todos os objetos são destruido ao fim do teste
    def setUp(self):
        self.response = requests.get('https://lista.mercadolivre.com.br/livros')
        self.content = self.response.content
        self.assert_frame_equal = assert_frame_equal
        self.ofertas = Produto.get_offers(self)

    #testando se está chegando um código da index
    def testHtmlFlaskIndex(self):
        application = app.test_client()
        response = application.get('/')
        self.assertNotEqual('ok',response.data.decode('utf-8'))
    
    #testando se o código da index é html
    def testConteudoCorretoIndex(self):
        application = app.test_client()
        response = application.get('/')
        self.assertIn('text/html', response.content_type)
    
    #testando se está chegando um código do produto
    def testHtmlFlaskProduto(self):
        aplicacion = app.test_client()
        response = aplicacion.get('/produto')
        self.assertNotEqual('ok',response.data.decode('utf-8'))
    
    #testando se o código do produto é html
    def testConteudoCorretoProduto(self):
        aplicacion = app.test_client()
        response = aplicacion.get('/produto')
        self. assertIn('text/html',response.content_type)

    #testando response que bate no mercado livre chcando o cod http 200
    def testResponseAPI(self):
        produtotest = Produto('livros')
        answer = produtotest.get_response()
        self.assertEqual(answer.status_code, 200)

    #testando o conteudo que o mercado livre retorna vendo se é um html
    def testContent(self):
        Produto.get_content(self)
        self.assertTrue('text/html',Produto.get_content(self))

    #testando a lista de ofertas montada checando se o tamnho edla é maior que 0
    def testOffers(self):
        Produto.get_offers(self)
        self.assertTrue(len(Produto.get_offers(self))>0)

    #testando dataframe comparando ele com uma df vazia(este teste em especifico vai retornar um fail)
    def testDataframe(self):
     Produto.get_dataframe(self)
     controle = pd.DataFrame({'a':[],'b':[],'c':[],'d':[]})
     self.assert_frame_equal(controle,Produto.get_dataframe(self))
    


if __name__ == '__main__':
    unittest.main()
