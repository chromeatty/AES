from pickle import TRUE
from encrypt import encrypt_text
from decryptor import decrypt_text
from functions import newTextFile, select_text_files
from keys import BUF_SIZE # import from keys

import os 
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes


# menu
while True:
    print("1. Create a new text file")
    print("2. Encrypt a selected text file")
    print("3. Decrypt a selected text file")
    print("4. Display text of text file")
    print("5. Display text of encrypted file")
    print("6. Display text of decrypted file")
    print("7. Exit menu")
    x = int(input("Select from 1 - 7: "))
    
    if x == 1:
        print("Create a new text file:")
        newTextFile()
    elif x == 2:
        print("Encrypt a selected text file:")
        #call to find .txt or .enc or .dec
        selected_text_file = select_text_files(".txt")

        if selected_text_file is not None:
            # Call your own encryption function with the selected_text_file
            print(f"Encrypting {selected_text_file}.")
            #encrypt the message and it will have the same file name but end in .enc instead of .txt
            encrypt_text(selected_text_file, str(selected_text_file[:-4]))
    
    elif x == 3:
        print("Decrypt a selected text file:")
        #call to find .txt or .enc or .dec
        #using .enc to find, in order to decrypt
        selected_text_file = select_text_files(".enc")

        if selected_text_file is not None:
            # Call your own encryption function with the selected_text_file
            print(f"Decrypting {selected_text_file}.")
            #encrypt the message and it will have the same file name but end in .enc instead of .txt
            decrypt_text(selected_text_file, str(selected_text_file[:-4]))
    elif x == 4:
       print("Display text of text file:")
       selected_text_file = select_text_files(".txt")
       f = open(selected_text_file, "r")
       print(f.read(BUF_SIZE))
       f.close()
    elif x == 5:
        print("Display text of encrypted file:")
        selected_text_file = select_text_files(".enc")
        f = open(selected_text_file, "rb")
        print(f.read(BUF_SIZE))
        f.close()
    elif x == 6:
        print("Display text of decrypted file:")
        selected_text_file = select_text_files(".dec")
        f = open(selected_text_file, "rb")
        print(f.read(BUF_SIZE))
        f.close()
    elif x == 7:
        print("Exiting the menu.")
        break
    else:
        print("Only select a number between 1 and 6.")


