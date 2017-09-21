import tkinter

def md4_encode():
    var = input_entry.get()
    result_text.insert('0.0','(md4)'+var)
def md5_encode():
    var = input_entry.get()
    result_text.insert('0.0','(md5)'+var)
def clear_text():
    result_text.delete('0.2')


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('encoder')
    window.geometry('500x500')
    #Here we need one entry , two button , one text
    input_entry = tkinter.Entry(window,show='*')
    #show=None ==> display normally
    input_entry.pack()

    md4_button = tkinter.Button(window,text='MD4 Encode',command=md4_encode)
    md4_button.pack()

    md5_button = tkinter.Button(window,text='MD5 Encode',command=md5_encode)
    md5_button.pack()

    clear_button = tkinter.Button(window,text='clear',command=clear_text)
    clear_button.pack()

    result_text = tkinter.Text(window,heigh=10)
    result_text.pack()

    window.mainloop()
