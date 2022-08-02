from pandas.testing import assert_frame_equal
import pandas as pd
import requests
import unittest
from model.product import Produto
from app import app


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.response = requests.get('https://lista.mercadolivre.com.br/livros')
        self.content = self.response.content
        self.assert_frame_equal = assert_frame_equal
        self.ofertas = Produto.get_offers(self)

    def testHtmlFlaskIndex(self):
        application = app.test_client()
        response = application.get('/')
        self.assertNotEqual('ok',response.data.decode('utf-8'))
    
    def testConteudoCorretoIndex(self):
        application = app.test_client()
        response = application.get('/')
        self.assertIn('text/html', response.content_type)
    
    def testHtmlFlaskProduto(self):
        aplicacion = app.test_client()
        response = aplicacion.get('/produto')
        self.assertNotEqual('ok',response.data.decode('utf-8'))
    
    def testConteudoCorretoProduto(self):
        aplicacion = app.test_client()
        response = aplicacion.get('/produto')
        self. assertIn('text/html',response.content_type)

    def testResponseAPI(self):
        produtotest = Produto('livros')
        answer = produtotest.get_response()
        self.assertEqual(answer.status_code, 200)

    def testContent(self):
        Produto.get_content(self)
        self.assertTrue('text/html',Produto.get_content(self))

    def testOffers(self):
        Produto.get_offers(self)
        self.assertTrue(len(Produto.get_offers(self))>0)

    def testDataframe(self):
     Produto.get_dataframe(self)
     controle = pd.DataFrame({'a':[],'b':[],'c':[],'d':[]})
     self.assert_frame_equal(controle,Produto.get_dataframe(self))
    


if __name__ == '__main__':
    unittest.main()
