#-*- coding: utf8 -*-

from random import randint


class RSA():
    _bytes=16
    text=""
    cipher=[]
    P,Q,E,D,N, phE = 0,0,0,0,0,0
    Ferma = []

    def __init__(self):
        super().__init__()
        self.text = ""
        self.cipher=[]
        self.Ferma = []      

    def generate_keys(self):
        self.P = self.get_simple_number()
        self.Q = self.get_simple_number()
        self.N = self.P*self.Q
        self.phE = (self.P-1)*(self.Q-1)
        self.generate_Ferma(self.phE)
        self.E = self.Ferma[randint(0, len(self.Ferma)-1)]
        self.D = self.modinv(self.E, self.phE)

        return {'E': self.E, 'D': self.D, 'N': self.N}

    def encrypt(self, E, N, text):
        self.text = text.encode('utf-16')

        for i in self.text:
            self.cipher.append(pow(i, E, N))
        
        for x in self.cipher:
            print(len(str(x)))
        
        return ' '.join([str(n) for n in self.cipher])

    def decrypt(self, D, N, cipher):
        self.cipher = [int(i) for i in cipher.split(' ')]
        text_blocks = [pow(c, D, N) for c in self.cipher]
        text = bytes(text_blocks)
        return text.decode('utf-16')

    def get_simple_number(self):
        binary = ''.join(['1' for x in range(self._bytes)])
        maxNumber = int(binary, 2)
        for i in range(0, maxNumber):
            randomNumber = randint(int(maxNumber/2), maxNumber)
            if self.checkSimple(randomNumber): return randomNumber
        raise ValueError("Can't find simple number")

    
    def checkSimple(self, n):
        for i in range(2, 256):
            if i == n: return True
            if (n%i) == 0: return False
        return True

    def generate_Ferma(self, n):
        for i in range(0, n):
            n1 = pow(2, i)
            n2 = pow(2, n1) + 1
            if n2 >= n: break

            self.Ferma.append(n2)

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = self.egcd(b%a,a)
        return (g, x - (b//a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise ValueError('No modular inverse')
        return x%m
        
if __name__ == "__main__":
    r = RSA()
    keys = r.generate_keys()
    print(keys)

    text = "привіт kitty !"
    print("text: %s" % text)

    cipher = r.encrypt(keys['E'], keys['N'], text)
    print("cipher: %s" % cipher)

    decipher = r.decrypt(keys['D'], keys['N'], cipher)
    print("Message: %s" % decipher)