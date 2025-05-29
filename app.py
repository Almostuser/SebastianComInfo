from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy  # Corrigido
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired  # Corrigido
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'  # Corrigido
db = SQLAlchemy(app)

# Modelo do produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem = db.Column(db.String(100), nullable=False)

# Formulário de produto
class ProdutoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    preco = DecimalField('Preço', validators=[DataRequired()])
    imagem = StringField('Imagem (nome do arquivo)', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

# Página inicial
@app.route('/')
def homepage():
    return render_template('index.html', titulo_pagina="SebastianCom")

# Listagem de produtos
@app.route('/produtos')
def produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)

# Cadastro de produto
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = ProdutoForm()
    if form.validate_on_submit():
        novo = Produto(  # Parênteses corrigidos
            nome=form.nome.data,
            preco=float(form.preco.data),
            imagem=form.imagem.data
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('produtos'))
    return render_template('cadastrar.html', form=form)

# Página de detalhes do produto
@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    return render_template('detalhes.html', produto=produto)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)