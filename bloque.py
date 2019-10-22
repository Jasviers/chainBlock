import json
import time
import hashlib as jas


class Bloque(object):
'''
'''
    def __init__(self, idx, trs, tmp, lastjas):
        self.idx = idx
        self.trans = trans
        self.tmp = tmp
        self.lastjas = lastjas
        self.nonce = 0


    def jascode(self):
        json_block = json.dupms(self.__dict__, sort_keys=True)
        return jas.sha256(json_block.encode()).hexdigest()

