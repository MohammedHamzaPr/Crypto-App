from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from webbrowser import open_new_tab
from os import mkdir,getcwd,path
from hashlib import md5
from threading import Thread
from time import sleep
from os import system
import base64
import marshal
#####################################
class main(Tk):
    def Window_settings(self):
        #Window settings
        self.title('Crypto')
        self.iconbitmap(f'{getcwd()}/src/2.ico')
        self.geometry('520x320+350+200')
        self.config(background='silver')
        self.var = IntVar()
        self.Closed = 50
    def check(self):
        while True:
            sleep(0.7)
            if self.Closed == True:
                break
            else:
                self.Check = self.var.get()
                if self.Check == 1 and self.com.get() == 'md5':
                    messagebox.showerror('Error Mode','you can\'t using Python File with md5')
                    self.com.set('base64 m85')
        #Fouctions
    def Select(self):
        self.fileName = filedialog.askopenfilename(title='select python file : Crypto',filetypes=(('All','*.*'),('Text File','*.txt'),('Python','*.py'),('Python without conaole','*.pyw'),('Java','*.java')))
        self.size = len(self.fileName.split('/'))
        self.filepath.delete(last=END,first=0)
        self.filepath.insert(0,self.fileName.split('/')[self.size-1])
        self.plinecode = open(self.fileName,'r',encoding='utf-8').read()
        self.name = self.fileName.split('/')[self.size-1]

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.Closed = True
            self.destroy()

    def shoel(self):
        open_new_tab('https://www.facebook.com/toxiccode12')
        open_new_tab('https://www.youtube.com/@Toxic_Code')
        open_new_tab('https://t.me/Toxic_Code')
        open_new_tab('https://t.me/toxiccode12')
        open_new_tab('https://toxiccode12.blogspot.com')
        open_new_tab('https://www.instagram.com/toxiccode12')

    def Encrypt(self):
        def En():
            if path.exists(getcwd()+'\\results') != True:
                try:
                    mkdir('results')
                except PermissionError:
                    system('mkdir("results")')
            if len(self.filepath.get()) < 2:
                messagebox.showerror('File','you forget select a file')
            self.crypto = self.com.get()
            if self.crypto == 'md5':
                c = md5(string=b'hi')
                newfile = open(f'{getcwd()}\\results\\__{self.name}','w')
                newfile.write(f'#Coding By Toxic Code\n{str(c.digest())}')
                newfile.close()
                messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{self.name}')
            elif self.crypto == 'base64 m85':
                newfile = open(f'{getcwd()}\\results\\__{self.name}','w')
                c = base64.a85encode(self.plinecode.encode('utf-8'))
                if self.Check == 1:
                    newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.a85decode({str(c)}))')
                else:
                    newfile.write('#Coding By Toxic Code\n')
                    newfile.write(str(c))
                newfile.close()
                messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{self.name}')
            elif self.crypto == 'base64 m64':
                newfile = open(f'{getcwd()}\\results\\__{self.name}','w')
                c = base64.b64encode(self.plinecode.encode('utf-8'))
                if self.Check == 1:
                    newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.b64decode({str(c)}))')
                else:
                    newfile.write('#Coding By Toxic Code\n')
                    newfile.write(str(c))
                newfile.close()
                messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{self.name}')
            elif self.crypto == 'base64 m32':
                newfile = open(f'{getcwd()}\\results\\__{self.name}','w')
                c = base64.b32encode(self.plinecode.encode('utf-8'))
                if self.Check == 1:
                    newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.b32decode({str(c)}))')
                else:
                    newfile.write('#Coding By Toxic Code\n')
                    newfile.write(str(c))
                newfile.close()
                messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{self.name}')
            elif self.crypto == 'base64 m16':
                newfile = open(f'{getcwd()}\\results\\__{self.name}','w')
                c = base64.b16encode(self.plinecode.encode('utf-8'))
                if self.Check == 1:
                    newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.b16decode({str(c)}))')
                else:
                    newfile.write('#Coding By Toxic Code\n')
                    newfile.write(str(c))
                newfile.close()
                messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{self.name}')
            elif self.crypto == 'marshal':
                newfile = open(f'{getcwd()}\\results\\__{self.name}','w')
                c = marshal.dumps(self.plinecode.encode('utf-8'))
                if self.Check == 1:
                    newfile.write(f'import marshal\n#Coding By Toxic Code\nexec(marshal.loads({str(c)}))')
                else:
                    newfile.write('#Coding By Toxic Code\n')
                    newfile.write(str(c))
                newfile.close()
                messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{self.name}')
        Thread(target=En).start()



    def CC(self):
        self.CCl = Label(self,text='Copyright Toxic Code',bg='black',fg='red',font=('Georgia 15'))


    def ICON(self):
        self.imgFile = PhotoImage(file=f'{getcwd()}/src/shield.png')
        self.imgFile = self.imgFile.subsample(4,4)
        self.imageicon = Label(self,image=self.imgFile,bg='silver')

    def Check_Button(self):
        self.isPtrhon = Checkbutton(self,text='Python File',variable=self.var,bg='silver')


    def Buttons(self):
        self.select = Button(self,text='Select File',bg='gold',fg='blue',font=5,activebackground='silver',command=self.Select)
        self.CryptoB = Button(self,text='Encryption',bg='gold',fg='blue',font=5,activebackground='silver',command=self.Encrypt)
        self.About = Button(self,text='About',bg='gold',fg='blue',font=5,activebackground='silver',command=self.shoel)

    def Labels(self):
        self.filepath = Entry(self,bg='black',fg='red',font='bold')



    def ComboBox(self):
        self.com = ttk.Combobox(
            self,
            values=('md5','base64 m85','base64 m64','base64 m32','base64 m16','marshal'),
            state='readonly'
        )
        self.com.current(0)

        #pack
    def __init__(self):
        super().__init__()
        self.ICON()
        self.Window_settings()
        self.CC()
        self.Buttons()
        self.Labels()
        self.Check_Button()
        self.ComboBox()
        self.CryptoB.place(x=70,y=230)
        self.com.place(x=170,y=230)
        self.filepath.place(y=170,x=170,width=170,height=28)
        self.select.place(x=70,y=170)
        self.isPtrhon.place(x=400,y=230)
        self.About.place(x=400,y=170)
        self.imageicon.pack()
        self.CCl.pack(fill='x',side='bottom')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        Thread(target=self.check).start()
        self.mainloop()
main()