from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', titulo_pagina="SebastianCom")

@app.route('/produtos')
def listar_produtos():
    produtos_exemplo = [
        {"id": 1, "nome": "Mouse Gamer XYZ", "preco": "R$ 150,00", "imagem": "mouse.jpg"},
        {"id": 2, "nome": "Teclado Mecânico ABC", "preco": "R$ 350,00", "imagem": "teclado.jpg"},
        {"id": 3, "nome": "Monitor LED 24 polegadas", "preco": "R$ 950,00", "imagem": "monitor.jpg"}
    ]
    return render_template('produtos.html', titulo_pagina="Produtos - SebastianCom", produtos=produtos_exemplo)

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    return f"Detalhes do produto com ID: {produto_id}. (Página a ser construída)"

if __name__ == '__main__':
    app.run(debug=True)
