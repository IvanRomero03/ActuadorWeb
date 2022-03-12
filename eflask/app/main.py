from flask import Flask
from eflask.app.ConectorDB import BaseDeDatos

app = Flask(__name__)


@app.route('/')
def home_view():
    DB = BaseDeDatos()
    DB.insertarRegistro(1)
    print(DB.selectRegistrosUsuario(1))
    return str(DB.selectRegistrosUsuario(1)[-1][1])
