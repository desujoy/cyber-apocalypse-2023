# write a program to decrypt rsa with n,e,c

from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes

class RSA:
    def __init__(self, n, e, c):
        self.n = n
        self.e = e
        self.c = c
    
    def decrypt(self):
        m = pow(self.c, self.e, self.n)
        return long_to_bytes(m)
    
rsa=RSA(0,0,0)

rsa.n = 7117896367308347186104494216886523527047132467965538031432510797175778124833495020819950855424085836071521229344832560764573133200641389725802130732709661
rsa.e = 3
rsa.c =  70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053

print(rsa.decrypt())

