import tkinter as tk
#tkinter is a Python GUI build-in package
import datetime

def change_time():
    global var
    if(var.get() == ''):
        var.set((str)(datetime.datetime.now()))
    else:
        var.set('')

if __name__=='__main__':
    window = tk.Tk()
    #create a tkinter.Tk object
    window.title('CurrentTime')
    #Set the title
    window.geometry('550x600')
    #Set the size of window

    var = tk.StringVar()
    var.set((str)(datetime.datetime.now()))
    #tkinter.StringVar() is a variable of tkinter
    l = tk.Label(window,textvariable=var,bg='green',font=('Arial',15),width=30,heigh=20)
    l.pack()
    #Create a label and pack
    b = tk.Button(window,text="Press me to get time",width=30,heigh=2,font=('Arial',12),command=change_time)
    b.pack()

    window.mainloop()
    #With tkinter.Tk().mainloop() the window will keep updating otherwise it won't refresh
