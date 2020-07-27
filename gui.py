import tkinter
from tkinter import messagebox
top = tkinter.Tk()

def helloCallBack():
    messagebox.showinfo("Message" , "Hello World!"  )
    
B = tkinter.Button(top, text ="Click Me!", command = helloCallBack)
        
B.pack()
top.mainloop()
