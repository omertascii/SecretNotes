import tkinter
from tkinter import messagebox, INSERT, END
from cryptography.fernet import Fernet
import base64

screen = tkinter.Tk()
screen.title("Secret Notes")
screen.config(pady=80,padx=50)





my_label = tkinter.Label(text="Enter your title")
my_label.pack()

file_name = tkinter.Entry()
file_name.pack()

my_label2 = tkinter.Label(text="Enter your secret")
my_label2.pack()

my_note = tkinter.Text()
my_note.config(width=40,height=20)
my_note.pack()

my_label3 = tkinter.Label(text="Enter a master key")
my_label3.pack()

password = tkinter.Entry()
password.pack()


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def savebutton_click():
    num1 = file_name.get()
    num2 = my_note.get("1.0", END)
    num3 = password.get()
    if num1 == "" or num2 == "" or num3 == "":
        messagebox.showinfo(title="Message",message="Boş alanları doldurunuz")
    else:
        mynote_encrypted = encode(num3,num2)
        secret = open("mysecret.txt",mode="a")
        secret.write(num1)
        secret.write("\n")
        secret.write(mynote_encrypted)
        secret.write("\n")
        file_name.delete(0, END)
        my_note.delete("1.0", END)
        password.delete(0, END)

def decypt_button():
    num1 = my_note.get("1.0", END)
    num2 = password.get()
    if num1 == "" or num2 =="":
        messagebox.showinfo(title="Hata!",message="Boş alanları doldurunuz")
    else:
        try:
            decyrpted_message = decode(num2,num1)
            my_note.delete("1.0", END)
            my_note.insert("1.0",decyrpted_message)
        except:
            messagebox.showinfo(title="Hata!",message="Şifrelenmemiş Metni Çözmeye Çalışma!")

file_save = tkinter.Button(text="Save",width=20,command=savebutton_click)
file_save.pack()

decrypt = tkinter.Button(text="Decrypt",width=10,command=decypt_button)
decrypt.pack()


tkinter.mainloop()