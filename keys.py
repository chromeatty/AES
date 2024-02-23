import os 
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes

#validate to see if the key and iv already exist if not create one.
if os.path.isfile("AES.key") == True & os.path.isfile("AES.iv") == True:
    f = open("AES.key", 'rb')
    key = f.read()
    f.close()

    f = open("AES.iv", 'rb')
    iv = f.read()
    f.close()

else:    
    key = os.urandom(32)
    iv = os.urandom(16)

    f = open("AES.key", 'wb')
    f.write(key)
    f.close()

    f = open("AES.iv", 'wb')
    f.write(iv)
    f.close()

cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()
BUF_SIZE = 1024 #this will go like so: read(BUF_SIZE)