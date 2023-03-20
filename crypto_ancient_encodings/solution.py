from Crypto.Util.number import long_to_bytes
from base64 import b64decode

def decode():
    with open("output.txt", "r") as f:
        encoded_flag = f.read()
    flag=b64decode(long_to_bytes(int(encoded_flag, 16)))
    print(flag.decode())

if __name__ == "__main__":
    decode()