import pandas as pd
import unittest
from model.product import Produto
from app import app


class TestProduct(unittest.TestCase):
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
        produtotest = Produto('miband')
        answer = produtotest.get_response()
        conteudo = answer.get_content()
        print(conteudo)
        

        # eu n lembro o que vem em conteudo, checar isso ai pra fazer o test

    def testOffers(self):
        # produtotest = Produto('cafe')
        # ofertinha = produtotest.get_offers()
        # self.assertIn('text/html', ofertinha)
        pass

    def testDataframe(self):
     pass


if __name__ == '__main__':
    unittest.main()
