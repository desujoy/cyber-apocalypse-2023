from os import urandom
from Crypto.Cipher import AES
#from secret import MESSAGE

#assert all([x.isupper() or x in '{_} ' for x in MESSAGE])


class Cipher:

    def __init__(self):
        self.salt = urandom(15)
        key = urandom(16)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]
    
    def decrypt(self, message):
        return [self.cipher.decrypt(c).decode().strip() for c in message]


def main():
    cipher = Cipher()
    #encrypted = cipher.encrypt(MESSAGE)
    #encrypted = "\n".join([c.hex() for c in encrypted])

    with open("output.txt", 'r') as f:
        output = f.read().strip().split("\n")
    
    decrypted = cipher.decrypt([bytes.fromhex(c) for c in output])
    decrypted = "".join(decrypted)

    with open("flag.txt", 'w+') as f:
        f.write(decrypted)


if __name__ == "__main__":
    main()
