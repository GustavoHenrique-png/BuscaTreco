import unittest
from model.product import Produto
from app import app


class TestProduct(unittest.TestCase):

    def setUp(self):
        application = app.test_client()
        aplicacion = app.test_client()
        self.response = aplicacion.get('/produto')
        self.response = application.get('/')

    def testHtmlFlaskIndex(self):
        self.assertNotEqual('ok',self.response.data.decode('utf-8'))
    
    def testConteudoCorretoIndex(self):
        self.assertIn('text/html', self.response.content_type)
    
    def testHtmlFlaskProduto(self):
        self.assertNotEqual('ok',self.response.data.decode('utf-8'))
    
    def testConteudoCorretoProduto(self):
        self.assertIn('text/html',self.response.content_type)

    def testResponseAPI(self):
        produtotest = Produto('livros')
        answer = produtotest.get_response()
        self.assertEqual(answer.status_code, 200)

    def testContent(self):
        # produtotest = Produto('miband')
        # conteudo = produtotest.get_content()
        # self.assertNotEqual(len(conteudo), 1)
        pass

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
