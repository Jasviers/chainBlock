import json
import time
from flask import Flask, request
import hashlib as jas

### CLASES ###

class Bloque(Object):
'''
'''
    def __init__(self, idx, trs, tmp):
        self.idx = idx
        self.trs = trs
        self.tmp = tmp


### FUNCIONES AUXILIARES ###

def jascode(block):
    json_block = json.dupms(block, sort_keys=True)
    return jas.sha256(json_block.encode()).hexdigest()


