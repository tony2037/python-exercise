import tkinter
import imp

def module_search():
    module_path = imp.find_module(module_text.get("1.0",'end-1c'))
    result_text.insert('0.0',module_path)
    return module_path

if __name__=='__main__':
    window = tkinter.Tk()
    window.title('Find Module')
    window.geometry('550x550')

    module_text = tkinter.Text(window,width=30,heigh=10)
    module_text.pack()

    research_button = tkinter.Button(window,text='Search',width=5,heigh=2,command=module_search)
    research_button.pack()

    result_text = tkinter.Text(window,width=50,heigh=10,bg='yellow')
    result_text.pack()

    window.mainloop()
