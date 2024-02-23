from keys import encryptor, BUF_SIZE # import from keys
import os 
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes

#encrypting the text file
def encrypt_text(fileName, encFile_name):
    
    encFile = (encFile_name + ".enc")
    file = open(encFile, 'wb')
    with open(fileName,'rb') as file1:
        while True:
            data = file1.read(BUF_SIZE)
            #print(len(data))
            if(len (data) > 0):
                ct = encryptor.update(data)
                #writing the encrypted message into the file
                file.write(ct)
            else:
                break
    file.close()
    file1.close()