from selenium import webdriver
import datetime
import time
import tkinter
import multiprocessing

def webdriver_active(url='https://www.youtube.com/watch?v=RgKAFK5djSk',driver=None,driver_path='../../chrome driver/Chromedriver.exe'):
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
def change_time():
    global var
    temp = ''
    for i in range(16):
        temp  += ((str)(datetime.datetime.now())[i])
    var.set(temp)


def start(year='2017',month='09',date='22',hour='08',minute='00'):
    window = tkinter.Tk()
    window.title('Good morning')
    window.geometry('550x600')
    var = tkinter.StringVar()
    label = tkinter.Label(window,textvariable=var,bg='green',font=('Arial',15),width=30,heigh=10)
    label.pack()

    #driver = webdriver.Chrome('../../chrome driver/Chromedriver.exe')
    #driver.get('https://www.youtube.com/watch?v=RgKAFK5djSk')
    change_time()
    #refresh = multiprocessing.Process(target=change_time,args=())
    #refresh.start()
    #refresh.join()

    target_time=year+'-'+month+'-'+date+' '+hour+':'+minute
    while(True):
        if(var.get() == '2017-09-22 08:00'):
            driver = webdriver.Chrome('../../chrome driver/Chromedriver.exe')
            driver.get('https://www.youtube.com/watch?v=RgKAFK5djSk')
            break
        change_time()

    window.mainloop()


#2017-08-18 00:42:02.545696
