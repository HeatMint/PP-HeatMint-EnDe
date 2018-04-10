from Tkinter import *
from tkMessageBox import *
from decrypt import *
from encrypt import *


class cryptgui:
    def __init__(self, function='encrypt'):
        # main frame
        crypter = Tk()
        crypter.title(function)
        crypter.geometry('640x480')
        crypter_font = ('Arial', 16)
        crypter_before = Text(crypter, width=60, state='normal')
        crypter_before.place(anchor='n', relx=0.5, rely=0.05)

        def after_crypt(text="nope"):
            # GUI called after encryption, the encryption
            after = Tk()
            after.geometry("500x400")
            after_text = Text(after, width=60, state="normal")
            after_text.place(anchor='n', relx=0.5, rely=0.05)
            after_text.insert(1.0, text)
            after.wm_attributes('-topmost', 1)
            after.mainloop()

        def work():
            # the function called after the encryption was pressed
            keyPress()
            showinfo('Working', 'trying to get your stuff ready')
            word = crypter_before.get("0.0", "end")
            password = crypter_password.get()
            if function == 'encrypt':
                if password != "":
                    showinfo("Password", "Your decryption password is " + Encrypt.antigen(
                        password)) + "\n Please remember it. It will not be recorded anywhere after you press OK."
                after = Encrypt.mainencrypt(word, password)
                after_crypt(after.replace("\n", ""))
            else:
                after = Decrypt.maindecrypt(word.replace("\n", ""), password)
                print word
                after_crypt(after)

        def keyPress():
            # function called to validate password
            a = crypter_password.get()
            valid_password = ''
            for i in a:
                if i in '1234567890':
                    valid_password += i
                else:
                    pass
            if len(valid_password) > 4:
                valid_password = valid_password[0:4]
            if a != valid_password:
                invalid()
                crypter_password.delete(0, END)
                crypter_password.insert(0, valid_password)

        def invalid():
            showinfo('wrong input',
                     'the length of the password should be shorter than 4 and all of them are integers. I '
                     'automatically made some change to it.')

        crypter_password = Entry(crypter)
        crypter_password.place(anchor='s', relx=0.67, rely=0.83)
        crypter_before.insert(1.0, 'Pleas enter the words that you want ' + function + ' here.')
        # need complicate justify on function
        if function == 'encrypt':
            label_text = "Password here, if you want"
        else:
            label_text = "Password here, if you have"
        entry_info = Label(crypter, text=label_text)
        entry_info.place(anchor='s', relx=0.67, rely=0.89)
        # need function
        crypter_button = Button(crypter, text=function, font=crypter_font,
                                command=lambda: work())
        crypter_button.place(anchor='s', relx=0.27, rely=0.87)
        # mainloop
        crypter.mainloop()


if __name__ == "__main__":
    cryptgui()
