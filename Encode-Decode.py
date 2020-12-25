# import
from tkinter import *
import base64
import random, string
import pyperclip
from tkinter import messagebox

# function to generate a random key
def Generator():
    password = ''
    for y in range(11):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    private_key.set(password)

# function to encode message into base64
def Encode(key,message):
    enc=[]
    try: 
        for i in range(len(message)):
            key_c = key[i % len(key)]
            enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    except:
        messagebox.showerror("Invalid input", "Please enter the key")
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# function to decode base64 into message
def Decode(key,message):
    dec=[]
    try:
        message = base64.urlsafe_b64decode(message).decode()
    except:
        messagebox.showerror("ValueError", "String argument should contain only ASCII characters")

    try:
        for i in range(len(message)):
            key_c = key[i % len(key)]
            dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    except:
        messagebox.showerror("Invalid input", "Please enter the key")
    return "".join(dec)

# function to select the mode to use
def Mode():
    if(ch.get() == 1):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(ch.get() == 2):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')
        
# function to exit 
def Exit():
    root.destroy()
    
# function to clear the input and output
def Reset():
    Text.set("")
    private_key.set("")
    ch.set(0)
    Result.set("")

# function to copy the private key and output [ie. Key: (some key) Code: (some code)]
def Copy():
    pyperclip.copy("Key: " + private_key.get() +" Code: " +Result.get())

# main function
if __name__ == '__main__':
    # initialization
    root = Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Message Encode and Decode")

    # variables
    Text = StringVar()
    private_key = StringVar()
    mode = StringVar()
    Result = StringVar()
    ch = IntVar()
    
    Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()           #* header

    # Key block
    Label(root,  font = 'arial 12 bold', text ='KEY').place(x=60, y = 60)
    Entry(root,  font = 'arial 10', textvariable = private_key, bg ='ghost white').place(x=200, y = 60)
    Button(root, font = 'arial 10 bold', text= 'Generate key', command = Generator, bg = 'LightBlue', width = 10, padx=2, pady=2).place(x=375, y = 60)

    # Mode block
    Label(root, font = 'arial 12 bold', text ='MODE').place(x=60, y = 90)
    Radiobutton(root, text="Encode", value=1, variable=ch).place(x=200, y=90)
    Radiobutton(root, text="Decode", value=2, variable=ch).place(x=270, y=90)

    # Input block
    Label(root, font = 'arial 12 bold', text='MESSAGE').place(x= 60,y=120)
    Entry(root, font = 'arial 12', textvariable = Text, bg = 'ghost white', width=30).place(x=200, y = 120)

    # Output Block
    Entry(root, font = 'arial 12 bold', textvariable = Result, width=30, state="readonly").place(x=200, y = 155)

    # Button Block
    Button(root, font = 'arial 10 bold', text = 'RESULT', command = Mode,  bg = 'LightGray' ,width =10, padx=2, pady=2).place(x=60, y = 150)
    Button(root, font = 'arial 10 bold', text = 'RESET' , command = Reset, bg = 'LimeGreen' ,width =5, padx=2, pady=2).place(x=130, y = 200)
    Button(root, font = 'arial 10 bold', text = 'COPY'  , command = Copy,  bg = 'Yellow'    ,width =5, padx=2, pady=2).place(x=230, y = 200)
    Button(root, font = 'arial 10 bold', text = 'EXIT'  , command = Exit,  bg = 'OrangeRed' ,width =5, padx=2, pady=2).place(x=330, y = 200)

    root.mainloop()                         #* mainloop 