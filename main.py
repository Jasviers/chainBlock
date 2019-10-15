from flask import Flask, request
from bloque import Bloque
from chainBlock import ChainBlock
import requests


app = Flask(__name__)

chainBlock = ChainBlock()
    
