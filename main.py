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
window = Tk()

#Window settings
window.title('Crypto')
window.iconbitmap(f'{getcwd()}/src/2.ico')
window.geometry('520x320+350+200')
window.config(background='silver')
var = IntVar()
Closed = 50
def check():
    global Check
    while True:
        sleep(0.7)
        if Closed == True:
            break
        else:
            Check = var.get()
            if Check == 1 and com.get() == 'md5':
                messagebox.showerror('Error Mode','you can\'t using Python File with md5')
                com.set('base64 m85')
Thread(target=check).start()

#Fouctions
def Select():
    global plinecode
    global name
    fileName = filedialog.askopenfilename(title='select python file : Crypto',filetypes=(('All','*.*'),('Text File','*.txt'),('Python','*.py'),('Python without conaole','*.pyw'),('Java','*.java')))
    size = len(fileName.split('/'))
    filepath.delete(last=END,first=0)
    filepath.insert(0,fileName.split('/')[size-1])
    global plinecode
    try:
        plinecode = open(fileName,'r',encoding='utf-8').read()
    except:
        pass
    global name
    name = fileName.split('/')[size-1]

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        global Closed
        Closed = True
        window.destroy()

def shoel():
    open_new_tab('https://www.facebook.com/toxiccode12')
    open_new_tab('https://www.youtube.com/@Toxic_Code')
    open_new_tab('https://t.me/Toxic_Code')
    open_new_tab('https://t.me/toxiccode12')
    open_new_tab('https://toxiccode12.blogspot.com')
    open_new_tab('https://www.instagram.com/toxiccode12')

def Encrypt():
    def En():
        if path.exists(getcwd()+'\\results') != True:
            try:
                mkdir('results')
            except PermissionError:
                system('mkdir("results")')
        if len(filepath.get()) < 2:
            messagebox.showerror('File','you forget select a file')
        crypto = com.get()
        if crypto == 'md5':
            c = md5(string=b'hi')
            newfile = open(f'{getcwd()}\\results\\__{name}','w')
            newfile.write(f'#Coding By Toxic Code\n{str(c.digest())}')
            newfile.close()
            messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{name}')
        elif crypto == 'base64 m85':
            newfile = open(f'{getcwd()}\\results\\__{name}','w')
            c = base64.a85encode(plinecode.encode('utf-8'))
            if Check == 1:
                newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.a85decode({str(c)}))')
            else:
                newfile.write('#Coding By Toxic Code\n')
                newfile.write(str(c))
            newfile.close()
            messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{name}')
        elif crypto == 'base64 m64':
            newfile = open(f'{getcwd()}\\results\\__{name}','w')
            c = base64.b64encode(plinecode.encode('utf-8'))
            if Check == 1:
                newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.b64decode({str(c)}))')
            else:
                newfile.write('#Coding By Toxic Code\n')
                newfile.write(str(c))
            newfile.close()
            messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{name}')
        elif crypto == 'base64 m32':
            newfile = open(f'{getcwd()}\\results\\__{name}','w')
            c = base64.b32encode(plinecode.encode('utf-8'))
            if Check == 1:
                newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.b32decode({str(c)}))')
            else:
                newfile.write('#Coding By Toxic Code\n')
                newfile.write(str(c))
            newfile.close()
            messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{name}')
        elif crypto == 'base64 m16':
            newfile = open(f'{getcwd()}\\results\\__{name}','w')
            c = base64.b16encode(plinecode.encode('utf-8'))
            if Check == 1:
                newfile.write(f'import base64\n#Coding By Toxic Code\nexec(base64.b16decode({str(c)}))')
            else:
                newfile.write('#Coding By Toxic Code\n')
                newfile.write(str(c))
            newfile.close()
            messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{name}')
        elif crypto == 'marshal':
            newfile = open(f'{getcwd()}\\results\\__{name}','w')
            c = marshal.dumps(plinecode.encode('utf-8'))
            if Check == 1:
                newfile.write(f'import marshal\n#Coding By Toxic Code\nexec(marshal.loads({str(c)}))')
            else:
                newfile.write('#Coding By Toxic Code\n')
                newfile.write(str(c))
            newfile.close()
            messagebox.showinfo('TC',f'Done Encryption your file you can found in result dirctory by name __{name}')
    Thread(target=En).start()



#CC
CC = Label(window,text='Copyright Toxic Code',bg='black',fg='red',font=('Georgia 15'))


#ICON
imgFile = PhotoImage(file=f'{getcwd()}/src/shield.png')
imgFile = imgFile.subsample(4,4)
imageicon = Label(window,image=imgFile,bg='silver')

#Check Button
isPtrhon = Checkbutton(window,text='Python File',variable=var,bg='silver')


#Buttons
select = Button(window,text='Select File',bg='gold',fg='blue',font=5,activebackground='silver',command=Select)
CryptoB = Button(window,text='Encryption',bg='gold',fg='blue',font=5,activebackground='silver',command=Encrypt)
About = Button(window,text='About',bg='gold',fg='blue',font=5,activebackground='silver',command=shoel)

#Labels
filepath = Entry(window,bg='black',fg='red',font='bold')



#ComboBox
com = ttk.Combobox(
    window,
    values=('md5','base64 m85','base64 m64','base64 m32','base64 m16','marshal'),
    state='readonly'
)
com.current(0)

#pack
CryptoB.place(x=70,y=230)
com.place(x=170,y=230)
filepath.place(y=170,x=170,width=170,height=28)
select.place(x=70,y=170)
isPtrhon.place(x=400,y=230)
About.place(x=400,y=170)
imageicon.pack()
CC.pack(fill='x',side='bottom')
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
