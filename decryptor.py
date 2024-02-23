from keys import decryptor, BUF_SIZE # import from keys
import os 
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes

#decrypting the text file
def decrypt_text(encFile, decFile):
    
    decFile = (decFile + ".dec")
    file = open(decFile,"wb")
    with open(encFile,'rb') as file1:
        while True:
            data = file1.read(BUF_SIZE)
            #print(len(data))
            if(len (data) > 0):
                ct = decryptor.update(data)
                file.write(ct)
            else:
                break

    file.close()
    file1.close()