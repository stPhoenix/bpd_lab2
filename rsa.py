from random import randint


class RSA():
    _bytes=32
    text=""
    P,Q,E,D,N, phE = 0,0,0,0,0,0
    Ferma = []

    def __init__(self):
        super().__init__()
        self.P = self.get_simple_number()
        self.Q = self.get_simple_number()
        self.N = self.P*self.Q
        self.phE = (self.P-1)*(self.Q-1)
        self.generate_Ferma(self.phE)
        self.E = self.Ferma[randint(0, len(self.Ferma)-1)]
        self.D = self.modinv(self.E, self.phE)

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
        return False

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
        g, x, y = egcd(a, m)
        if g != 1:
            raise ValueError('No modular inverse')
        return x%m
        

RSA()