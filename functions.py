import os 
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes

def newTextFile():
    text = input("Write the text you would like to encrypt: ")
    #file_name = input("Write desired file name: ")
        
    while True:
        file_name = input("Write desired file name: ")

        # Check if the file already exists
        if os.path.isfile(file_name + ".txt"):
            print("File name already exists in the directory.")
        else:
            #text_automate if the file does not exist
            message = text
            f = open(file_name + ".txt", 'w')
            f.write(message)
            f.close()
            print("Encryption process completed.")
            break
          


#encrypt_or_decrypt input .txt or .enc or .dec to iterat through the list
def select_text_files(encrypt_or_decrypt, directory="."):
    
    text_files = [file for file in os.listdir(directory) if file.endswith(encrypt_or_decrypt)]

    if not text_files:
        print("No files found in the directory.")
        return None

    print("Files exist in the directory:")
    #iterate throgh existing files
    for i, file in enumerate(text_files, 1):
        print(f"{i}. {file}")

    selected_index = int(input("Select a file (enter the corresponding number): ")) - 1

    if 0 <= selected_index < len(text_files):
        selected_file = text_files[selected_index]
        #return the selected file
        return selected_file
    else:
        print("Invalid selection.")
        return None