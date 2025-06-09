from flask import Flask
from models import init_app
from controller.LojaController import loja_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados e modelos
init_app(app)

# Registra o Blueprint do controller
app.register_blueprint(loja_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)