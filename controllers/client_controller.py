from flask import Blueprint, render_template, request
from models.termino import TerminoModel

client = Blueprint('client', __name__)

@client.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '')
    if query:
        terminos = TerminoModel.buscar_terminos(query)
    else:
        terminos = TerminoModel.obtener_todos()
    return render_template('client/index.html', terminos=terminos, query=query)
