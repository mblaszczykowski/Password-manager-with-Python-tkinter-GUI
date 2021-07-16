from tkinter import *
import os

###############################
# Cryptographic part

import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

backend = default_backend()
iterations = 100_000

def _derive_key(password: bytes, salt: bytes, iterations: int = iterations) -> bytes:
    """Derive a secret key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iterations, backend=backend)
    return b64e(kdf.derive(password))

def password_encrypt(message: bytes, password: str, iterations: int = iterations) -> bytes:
    salt = secrets.token_bytes(16)
    key = _derive_key(password.encode(), salt, iterations)
    return b64e(
        b'%b%b%b' % (
            salt,
            iterations.to_bytes(4, 'big'),
            b64d(Fernet(key).encrypt(message)),
        )
    )

def password_decrypt(token: bytes, password: str) -> bytes:
    decoded = b64d(token)
    salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
    iterations = int.from_bytes(iter, 'big')
    key = _derive_key(password.encode(), salt, iterations)
    return Fernet(key).decrypt(token)

###############################





# Getting computer username
#import os.path
username = os.path.expanduser("~").split("/")[2]
print(username)



# Getting path to Documents folder
# If there are no password manager files in Documents, we create them

from sys import platform
if platform == "linux" or platform == "linux2":
    path = '/home/' + username + '/Documents/password_manager/'
    if os.path.isdir(path)!=True:
        os.mkdir(path)

    path_do_sprawdzenia1 = path + 'zawartosc/konta'

    if os.path.isdir(path_do_sprawdzenia1)!=True:
        os.mkdir(path+'zawartosc')
        os.mkdir(path+'zawartosc/konta')

    path_do_sprawdzenia2 = path + 'loginy'
    if os.path.isdir(path_do_sprawdzenia2)!=True:
        os.mkdir(path+'loginy')


elif platform == "darwin":
    path = '/Users/' + username +'/Documents/password_manager/'
    if os.path.isdir(path)!=True:
        os.mkdir(path)


    path_do_sprawdzenia1 = path + 'zawartosc/konta'

    if os.path.isdir(path_do_sprawdzenia1)!=True:
        os.mkdir(path+'zawartosc')
        os.mkdir(path+'zawartosc/konta')

    path_do_sprawdzenia2 = path + 'loginy'
    if os.path.isdir(path_do_sprawdzenia2)!=True:
        os.mkdir(path+'loginy')


elif platform == "win32":
    path = 'C:\\Users\\' + username + '\\Documents\\password_manager\\'
    if os.path.isdir(path)!=True:
        os.mkdir(path)


    path_do_sprawdzenia1 = path + 'zawartosc\\konta'

    if os.path.isdir(path_do_sprawdzenia1)!=True:
        os.mkdir(path+'zawartosc')
        os.mkdir(path+'zawartosc\\konta')

    path_do_sprawdzenia2 = path + 'loginy'
    if os.path.isdir(path_do_sprawdzenia2)!=True:
        os.mkdir(path+'loginy')







class App():
    def __init__(self):
        self.root = Tk()
        xx=300
        yy=400
        self.root.geometry('300x400+800+300')
        self.root.title("")
        self.root.iconbitmap(None)
        self.root.configure(background='white')
        
        #self.root.minsize(300,400)
        #self.root.maxsize(600,600)

        self.root.resizable(False, False)

        bgcolor = 'white'




        self.odstep = Label(self.root, bg='white')
        self.przywitanie = Label(self.root, text='hello!',fg='black', bg='white', font=("Baskerville", 44))

        self.loginentry = Entry(self.root, highlightbackground='white')

        self.hasloentry = Entry(self.root, highlightbackground='white', show="*")


        self.submit_login_button = Button(self.root, highlightbackground='white', text=">", command=self.pobierz_login, bg='white', activebackground='white')
        self.submit_loginihaslo_button = Button(self.root, highlightbackground='white', text=">", command=self.pobierz_haslo, bg='white', activebackground='white')

        self.registerbutton = Button(self.root, highlightbackground='white', text='create account', command=self.rejestracja, bg='yellow', background='yellow', activebackground='white', highlightcolor='white', bd=2)

        self.wrocbutton = Button(self.root, highlightbackground='white', text="<", command=self.wyswietl_logowanie)

        # By clicking escape you will always go to log in screen
        self.root.bind("<Escape>", self.wyswietl_logowanie)



        # ERROR MESSAGES

        self.zlehaslo = Button(text='Wrong password', highlightbackground='white', foreground='red')
        self.zlylogin = Button(text='Account with this login does not exist', highlightbackground='white', foreground='red')
        self.podajlogin = Button(text='Enter your login', highlightbackground='white', foreground='red')
        self.podajloginihaslo = Button(text='Enter login and password', highlightbackground='white', foreground='red')

        self.wczesniejzalogowano = False



        self.wyswietl_logowanie()

        self.root.mainloop()



    def nic(self, _Event=None):
        pass



    def rejestracja(self):
        self.zlehaslo.place(x=6000,y=10)
        self.zlylogin.place(x=6000,y=10)


        self.loginentry.place(x=6000, y=6000)
        self.hasloentry.place(x=6000, y=6000)
        self.submit_login_button.place(x=6000, y=6000)
        self.submit_loginihaslo_button.place(x=6000, y=6000)
        self.registerbutton.place(x=6000,y=6000)

        def createaccountdef():
            login = self.rejestracjalogin.get()
            haslo = self.rejestracjahaslo.get()


            if login != "" and haslo != "":


                # w zaleznosci od systemu
                if platform == "linux" or platform == "linux2":
                    sciezka = '/home/' + username + '/Documents/password_manager/loginy/'

                elif platform == "darwin":
                    sciezka = '/Users/' + username +'/Documents/password_manager/loginy/'

                elif platform == "win32":
                    sciezka = 'C:\\Users\\' + username + '\\Documents\\password_manager\\loginy\\'


                with open(sciezka+login+'.txt', 'w') as f:
                    pass



                # we create a content file in the future, but it must be immediately encrypted with anything, because then logging is whether the algorithm will decrypt it, if not it crashes the wrong password

                nic = ''

                # ENCRYPTING
                zaszyfrowanenic = password_encrypt(nic.encode(), haslo)


                # w zaleznosci od systemu
                if platform == "linux" or platform == "linux2":
                    sciezka = '/home/' + username + '/Documents/password_manager/zawartosc/konta/'

                elif platform == "darwin":
                    sciezka = '/Users/' + username +'/Documents/password_manager/zawartosc/konta/'

                elif platform == "win32":
                    sciezka = 'C:\\Users\\' + username + '\\Documents\\password_manager\\zawartosc\\konta\\'


                with open(sciezka + login+'.txt', 'wb') as f:
                    f.write(zaszyfrowanenic)
   





                self.rejestracjalogin.place(x=6000, y=6000)
                self.rejestracjahaslo.place(x=6000, y=6000)
                self.rejestracjawyslij.place(x=6000, y=6000)

                self.przywitanie.configure(text='hello!')
                self.wyswietl_logowanie()

            else:
                self.podajloginihaslo.place(x=75,y=40)




        self.przywitanie.configure(text='registration')

        self.odstep.place(x=6000,y=6000)
        self.przywitanie.place(x=6000,y=6000)

        self.wrocbutton.pack(pady=5)
        self.odstep.pack()
        self.przywitanie.pack(pady=15)

        self.rejestracjalogin = Entry(self.root, highlightbackground='white')
        self.rejestracjalogin.pack(pady=5)
        self.rejestracjalogin.focus()

        self.rejestracjahaslo = Entry(self.root, highlightbackground='white', show="*")
        self.rejestracjahaslo.pack(pady=0)

        self.rejestracjawyslij = Button(self.root, highlightbackground='white', text='create new account', command=createaccountdef)
        self.rejestracjawyslij.pack(pady=25)



    def wyswietl_logowanie(self, _Event=None):

        self.root.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())

        if self.wczesniejzalogowano == True:

            self.zapiszpoprzednitext()



        self.przywitanie.configure(text='hello!')

        #self.root.bind("<Escape>", self.nic)

        self.root.configure(background='white')

        self.podajloginihaslo.place(x=6000,y=40)

        try:
            self.wrocbutton.place(x=6000,y=6000)
        except: 
            pass

        try:
            self.scrollb.destroy()
        except:
            pass

        try:
            self.notetext.destroy()
            self.powrotbutton.destroy()
        except:
            pass

        try:
            self.canvas.destroy()
        except:
            pass

        try:
            self.rejestracjalogin.destroy()
            self.rejestracjahaslo.destroy()
            self.rejestracjawyslij.destroy()
        except:
            pass

        try:
            self.szukaj.destroy()

        except:
            pass

        try:
            self.stworzkonto.destroy()
        except:
            pass

        #self.loginentry.place(x=90, y=130)



        self.odstep.pack(pady=35)
        self.przywitanie.pack()
        self.loginentry.pack(pady=10)
        self.loginentry.focus()
        self.submit_login_button.pack(pady=10)
        self.registerbutton.pack(pady=40)



        self.loginentry.bind("<Return>", self.pobierz_login)



    def pobierz_login(self,_Event=None):
        self.login = self.loginentry.get()
        print("login: " + self.login)

        if self.login != "":
            import os
            docelowyplik = self.login + ".txt"

            jest = False

            # depending on the system
            if platform == "linux" or platform == "linux2":
                directory = '/home/' + username + '/Documents/password_manager/loginy'

            elif platform == "darwin":
                directory = '/Users/' + username +'/Documents/password_manager/loginy'

            elif platform == "win32":
                directory = 'C:\\Users\\' + username + '\\Documents\\password_manager\\loginy'
 

            for filename in os.listdir(directory):
                if filename == docelowyplik:
                    jest = True
  
                    print('jest login')


            if jest==False:

                self.zlehaslo.place(x=8000,y=10)
                self.podajlogin.place(x=6000,y=100)
                self.zlylogin.place(x=20,y=10)
                self.loginentry.focus()


            if jest==True:
                # when there will be a login in the database, we will show the password field
                self.zlylogin.place(x=6000,y=10)
                self.podajlogin.place(x=6000,y=10)

                # we are building a formation from the beginning
                self.submit_login_button.place(x=6000,y=6000)
                self.registerbutton.place(x=6000,y=6000)

                self.hasloentry.pack()
                self.hasloentry.focus()
                self.hasloentry.bind("<Return>", self.pobierz_haslo)

                self.submit_loginihaslo_button.pack(pady=10)
                self.registerbutton.pack(pady=30)

        else:
            #print("enter login")
            self.zlylogin.place(x=6000,y=10)
            self.podajlogin.place(x=80,y=10)


    def pobierz_haslo(self, _Event=None):
        self.haslo = self.hasloentry.get()

        self.loggedin(self.login)














    def zapiszpoprzednitext(self):
        # try because even if it is sometimes after logging in and someone clicks registration, it was an error
        try:
            trescc = self.notetext.get("1.0",END)

            if trescc!= "":
                # ENCRYPTING THERE
                zaszyfrowanatresc = password_encrypt(trescc.encode(), self.haslo)


                # w zaleznosci od systemu
                if platform == "linux" or platform == "linux2":
                    sciezka = '/home/' + username + '/Documents/password_manager/zawartosc/konta/'

                elif platform == "darwin":
                    sciezka = '/Users/' + username +'/Documents/password_manager/zawartosc/konta/'

                elif platform == "win32":
                    sciezka = 'C:\\Users\\' + username + '\\Documents\\password_manager\\zawartosc\\konta\\'


                with open(sciezka + self.cel, 'wb') as f:
                    f.write(zaszyfrowanatresc)

        except:
            pass



    def loggedin(self, login):

        self.zlehaslo.place(x=6000,y=10)
        self.zlylogin.place(x=6000,y=10)


        self.loginentry.delete(0, END)
        self.hasloentry.delete(0, END)



        #self.root.configure(background='black')
        import os
        self.loginentry.place(x=6000, y=6000)
        self.hasloentry.place(x=6000, y=6000)
        self.submit_loginihaslo_button.place(x=6000, y=6000)
        self.registerbutton.place(x=6000, y=6000)
        self.przywitanie.place(x=6000,y=6000)
        self.odstep.place(x=5000,y=6000)


        self.cel = login + ".txt"
        '''
        directory = '/Users/michvl/Documents/___Projects/Programming/passwords gui/loginy'
        
        znalezione = False
        for filename in os.listdir(directory):
            if filename == cel:
                znalezione = True

        if znalezione==False:
            with open("zawartosc/" + cel, 'w') as f:
                pass
        '''


        # funkcjeeee


        def odczytaj():

            # w zaleznosci od systemu
            if platform == "linux" or platform == "linux2":
                sciezka = '/home/' + username + '/Documents/password_manager/zawartosc/konta/'

            elif platform == "darwin":
                sciezka = '/Users/' + username +'/Documents/password_manager/zawartosc/konta/'

            elif platform == "win32":
                sciezka = 'C:\\Users\\' + username + '\\Documents\\password_manager\\zawartosc\\konta\\'



            with open(sciezka + self.cel, 'r') as f:
                zawartosc = f.read()




            # DECRYPTING THERE
            try:
                zawartoscodszyfrowana = password_decrypt(zawartosc, self.haslo).decode()
                self.notetext.delete('1.0', END)
                self.notetext.insert('1.0', zawartoscodszyfrowana)

                self.wczesniejzalogowano = True

            except Exception as e:
                print(e)

                print('error')
                self.zlehaslo.place(x=80,y=10)
                self.wyswietl_logowanie()









        def zapisznawyjscie(_Event=None):


            trescc = self.notetext.get("1.0",END)



            if trescc!= "":
                # ENCRYPTING THERE
                zaszyfrowanatresc = password_encrypt(trescc.encode(), self.haslo)


                # w zaleznosci od systemu
                if platform == "linux" or platform == "linux2":
                    sciezka = '/home/' + username + '/Documents/password_manager/zawartosc/konta/'

                elif platform == "darwin":
                    sciezka = '/Users/' + username +'/Documents/password_manager/zawartosc/konta/'

                elif platform == "win32":
                    sciezka = 'C:\\Users\\' + username + '\\Documents\\password_manager\\zawartosc\\konta\\'



                with open(sciezka + self.cel, 'wb') as f:
                    f.write(zaszyfrowanatresc)


            self.root.destroy()





        def search(_Event=None):


            self.notetext.tag_remove('found', '1.0', END)
            #if wyszukane==False:
            
            s = self.searchent.get() # Grabs the text from the entry box
            if s:
                idx = '1.0'
                while 1:
                    idx = self.notetext.search(s, idx, nocase=1, stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(s))
                    self.notetext.tag_add('found', idx, lastidx)
                    idx = lastidx
                    self.notetext.see(idx)  # Once found, the scrollbar automatically scrolls to the text
                self.notetext.tag_config('found', background='yellow')
                    
            self.searchent.focus_set()


        def wyszukaj(_Event=None):
        
            if self.czywyszukane==False:
                self.searchent.focus()
                self.searchent.place(x=50, y=5, height=30, width=100)
                self.czywyszukane = True
            else:
                self.notetext.focus()
                self.searchent.place(x=5000, y=10, height=40, width=100)

                self.notetext.tag_remove('found', '1.0', END)
                
                self.czywyszukane=False


        global kliknieteee
        kliknieteee = False
        def pokazsearchent():
            global kliknieteee

            if kliknieteee==False:

                kliknieteee = True
                self.searchent.place(x=110,y=2)
                self.searchent.focus()

            else:

                self.notetext.tag_remove('found', '1.0', END)
                self.searchent.place(x=6000,y=0)
                self.searchent.delete(0, END)

                kliknieteee = False



        # end of local functions

        self.notetext = Text(self.root, bd=0, highlightbackground='white', highlightthickness=0,font=('SF Text', 16), bg='white', fg='black')
        
        self.scrollb = Scrollbar(self.root, command=self.notetext.yview, width=14)
        self.notetext['yscrollcommand'] = self.scrollb.set

        self.scrollb.place(x=286,y=34, height=360)



        self.szukaj = Button(self.root, text='search', highlightbackground='white', command=pokazsearchent)
        self.szukaj.place(x=215,y=0)
        


        self.searchent = Entry(self.root, width=10, highlightbackground='white')


        self.searchent.bind("<Return>", search)
        self.searchent.bind("<Control-f>", wyszukaj)



        #self.nazwakontalabel = Label(self.root, text='nazwa konta: ')
        #self.nazwakontalabel.place(x=10, y=20)

        prr = ('SF Text', 10)



   

        #self.haslodokontalabel = Label(self.root, text='haslo: ')


        





        self.wrocbutton.place(x=2, y=0)
        


        self.notetext.place(x=4, y=38, width=285, height=360)






        self.canvas = Canvas(self.root, bg='white', bd=0, highlightbackground='white')
 
        # This creates a line of length 200 (straight horizontal line)
        self.canvas.create_line(0, 5, 300, 5, fill='gray')
 
         
        # This pack the canvas to the main window and make it expandable
        self.canvas.place(x=0,y=29, width=300, height=9)

        





        self.root.protocol("WM_DELETE_WINDOW", zapisznawyjscie)

        odczytaj()


        

        




App()