import tkinter
from tkinter import messagebox, INSERT, END
from cryptography.fernet import Fernet


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




def savebutton_click():
    num1 = file_name.get()
    num2 = my_note.get("1.0", END)
    num3 = password.get()
    if num1 == "" or num2 == "" or num3 == "":
        messagebox.showinfo(title="Message",message="Boş alanları doldurunuz")
    else:
        secret = open("mysecret.txt",mode="a")
        secret.write(num1)
        secret.write("\n")
        secret.write(num2)
        secret.write("\n")
        file_name.delete(0, END)
        my_note.delete("1.0", END)
        password.delete(0, END)


file_save = tkinter.Button(text="Save",width=20,command=savebutton_click)
file_save.pack()

decrypt = tkinter.Button(text="Decrypt",width=10)
decrypt.pack()


tkinter.mainloop()