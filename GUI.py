from Tkinter import *
from tkMessageBox import *
from crypter import *


def mainGUI():
    # main frame
    global root
    root = Tk()
    root.geometry('800x500')
    root.title('HeatMint Ee/Decrypter GUI V0.1')
    root.minsize(800, 500)
    root.maxsize(800, 500)
    # Title
    title_font = ('arial', 32)
    title = Label(root, text='What can I do 4 U?', font=title_font)
    title.place(anchor='e', rely=0.2, relx=0.75)
    # ecryption button part
    encrypt_font = ('Arial', 50)
    encrypt = Button(root, text='encrypter', font=encrypt_font, height=3, bg='grey', fg='white',
                     command=lambda: cryptgui('encrypt'))
    encrypt.place(relx=0.06, rely=0.67, anchor='w')
    # decryption button part
    decrypt_font = ('Arial', 50)
    decrypt = Button(root, text='decrypter', font=decrypt_font, height=3, bg='grey', fg='white',
                     command=lambda: cryptgui('decrypt'))
    decrypt.place(relx=0.51, rely=0.67, anchor='w')
    # info button part(needs to complete)
    info_font = ('Arial', 12)
    infos = 'Personal Project'
    info = Button(root, text='Big Red\nButton!', font=info_font, bg='red', fg='white',
                  command=lambda: showinfo('software info', infos))
    info.place(anchor='e', relx=1, rely=0.05)
    # mainloop
    root.mainloop()


def crypterGUI():
    # main frame
    global crypter
    crypter = Tk()
    crypter.geometry('600x400')
    crypter_font = ('Arial', 16)
    crypter_button = Button(crypter, text='Mike', font=crypter_font)
    crypter_button.place(anchor='s', relx=0.5, rely=0.5)
    crypter_before = Entry(crypter, width=60, state='normal')
    crypter_before.place(anchor='n', relx=0.5, rely=0.05)
    # mainloop
    crypter.mainloop()


mainGUI()
