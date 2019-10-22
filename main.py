from flask import Flask, request
from bloque import Bloque
from chainBlock import ChainBlock
import requests
import time


app = Flask(__name__)

chainBlock = ChainBlock()


@app.route('/transaccion', methods=['POST'])
def nueva_trans():
    req = request.get_json()
    requirements = ["autor", "transaccion"]
    for r in requirements:
        if not req.get(r):
            return "Transaccion no valida", 404

    req['tmp'] = time.time()

    chainBlock.add_trans(req)
    return "Success", 201


@app.route('/cadena', methods=['GET'])
def get_cadena():
    cad = []
    for b in chainBlock.chain:
        cad.append(b.__dict__)
    return json.dumps({'length':len(cad), 'chain':cad})


@app.route('/minar', methods=['GET'])
def minado():
    res = chainBlock.mina()
    return f'Bloque #{res} minado' if res else "El bloque no fue minado"

app.run(debug=True, port=8895)
