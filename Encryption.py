from cryptography.fernet import Fernet
from tkinter import *

root = Tk()
root.title("Welcome to the file encryption program")
root.geometry('800x800')


filename_string = None
# function to display user text when
# button is clicked
def clicked():
    filename_string = str(txt.get())

    def generate_key():
        return Fernet.generate_key()

    def write_key_to_file(key, filename):
        with open(filename, 'wb') as key_file:
            key_file.write(key)

    def load_key_from_file(filename):
        with open(filename, 'rb') as key_file:
            return key_file.read()

    def encrypt_file(key, filename, output_filename):
        with open(filename, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        with open(output_filename, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(key, filename, output_filename):
        with open(filename, 'rb') as f:
            encrypted_data = f.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(output_filename, 'wb') as f:
            f.write(decrypted_data)

    key = generate_key()
    write_key_to_file(key, 'secret key')

    encrypt_file(key, filename_string + '.txt', 'encrypted.txt')
    decrypt_file(key, 'encrypted.txt', 'decrypted.txt')





btn = Button(root, text="Encrypt/Decrypt",
             fg="red", command=clicked)
btn.grid(column=2, row=0)

txt = Entry(root, width=10)
txt.grid(column =1, row =0)

root.mainloop()