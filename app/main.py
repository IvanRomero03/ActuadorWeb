from flask import Flask
from app.ConectorDB import BaseDeDatos

app = Flask(__name__)


@app.route('/')
def home_view():
    DB = BaseDeDatos()
    DB.insertarRegistro(1)
    return '<h1>Hola mundo</h1>'
