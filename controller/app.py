from flask import Flask, render_template, request, redirect, url_for
# import sys
# sys.path.append('../model')
from model.product import Produto
# instância da classe flask
app = Flask(__name__, template_folder='../template')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
     #produto_buscado = request.form['product']
     return redirect(url_for('produto'))


@app.route('/produto', methods=['GET', 'POST'])
def product():
    produto = request.form['product']
    novo_produto = Produto(produto)
    novo_produto.get_response()
    novo_produto.get_content()
    novo_produto.get_offers()
    novo_produto.get_dataframe()
    return render_template('produto.html', tables=[novo_produto.dataframe.to_html(classes='data', header=True)])


# Checando se o usuário está acessando o programa principal
if __name__ == '__main__':
    app.run(debug=True)
