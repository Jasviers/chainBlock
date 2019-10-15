import time
from bloque import Bloque

class ChainBlock(Object):
    '''
    '''
    def __init__(self):
        self.trans_stack = []
        self.dif = 1
        self.chain = []
        self._genesis()


    def _genesis(self):
        genesisB = Bloque(0, [], time.time(), '0')
        genesisB.jas = genesisB.jascode()
        self.chain.append(genesisB)

    
    @property
    def ultimo(self):
        return self.chain[-1]


    def proletario(self, b):
        new_jas = b.jascode()
        while not new_jas.startswith('0' * self.dif):
            b.nonce += 1
            new_jas = b.jascode()
        return new_jas


    def add(self, b, pru):
        anteriorB = self.ultimo.jas

        if anteriorB != b.lastjas or not self._valid(b, pru):
            return false
        
        b.jas = pru
        self.chain.append(b)
        return True


    def _valid(self, b, pru):
        return pru.startswith('0' * self.dif) and pru == b.jascode()


    def add_trans(self, new_trans):
        self.trans_stack.append(new_trans)


    def mina(self):
        if not self.trans_stack:
            return False

        ultimo = self.ultimo

        nb = Block(ultimo.idx+1,
                self.trans_stack,
                time.time(),
                ultimo.jas)

        pru = self.proletario(nb)
        self.add(nb, pru)
        self.trans_stack = []
        return nb.idx
