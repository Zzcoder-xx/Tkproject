# -*- codeing = utf-8 -*-
# @Time : 2020/6/26 0026 21:20
# @Author : Zz
# @File : GuiTest.PY
# @Software : PyCharm
import os


import tkinter as tk
import tkinter.font as tf
import json
import datetime
import dateutil.parser
import decimal
import pyttsx3
import threading
import pythoncom

from Data import getData
from Th import fun

'''
def fun():
    pythoncom.CoInitialize()
    a = rec()
    if a == 1:
        saudi()
    else:
        print(a)
    pythoncom.CoUninitialize()

    timer = threading.Timer(60, fun)
    timer.start()


def rec():
    for i in getData():
        h, m = main(i)
        curr_time = datetime.datetime.now()+datetime.timedelta(seconds=-7)
        if curr_time.hour == h and curr_time.minute == m and i in getData():
            print("时间到" + str(datetime.datetime.now()))
            return 1
        print(i+str(curr_time))
    print("------------------------"+"\n")


def saudi():
    curr_time = datetime.datetime.now()
    engine = pyttsx3.init()
    msg = '现在是,' + str(curr_time.year) + '年' + str(curr_time.month) + '月' + str(curr_time.day) + '日' + str(
        curr_time.hour) + '点' + str(curr_time.minute) + '分'+str(curr_time.second)+'，抄表时间到'

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.25)
    engine.say(msg)
    print(msg)
    # engine.say('黄湘欣傻B')
    # 运行并且等待
    engine.runAndWait()

def getData():
    with open("config.json",encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
    return config


CONVERTERS = {
    'datetime': dateutil.parser.parse,
    'decimal': decimal.Decimal,
}


class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime,)):
            return {"val": obj.isoformat(), "_spec_type": "datetime"}
        elif isinstance(obj, (decimal.Decimal,)):
            return {"val": str(obj), "_spec_type": "decimal"}
        else:
            return super().default(obj)


def object_hook(obj):
    _spec_type = obj.get('_spec_type')
    if not _spec_type:
        return obj

    if _spec_type in CONVERTERS:
        return CONVERTERS[_spec_type](obj['val'])
    else:
        raise Exception('Unknown {}'.format(_spec_type))


def main(i):

    data = getData()

    thing = json.dumps(data, cls=MyJSONEncoder)

    a = json.loads(thing, object_hook=object_hook)

    y = a[i]

    #print(y)


    time = datetime.datetime.strptime(y, "%H:%M")
    #time = thing['thing']

    return time.hour,time.minute
'''
def ctrlEvent(event):
    if (12 == event.state and event.keysym == 'c'):
        return
    else:
        return "break"



window = tk.Tk()

window.title('定时抄表服务')

# window.geometry('500x300')

window.resizable(False, False)

ft = tf.Font(size=20)


def begin(x):
    a = 1
    b = len(getData())
    msg = getData()

    for i in getData():

        # j =str(i)
        # print(msg[j])
        # t=tk.Text(window,width=10,height=1,font=ft)
        d = tk.Text(window, width=5, height=1, font=ft)
        #print(i)

        d.bind("<Key>", lambda a: ctrlEvent)
        d.insert("insert", msg[i])
        d["state"] = 'disabled'
        l = tk.Label(window, text=i,width=10, height=1)
        # t.grid(row=i,column=1)
        if a <= b:
            l.grid(row=1, column=a, padx=8, pady=4)
            d.grid(row=2, column=a, padx=8, pady=4)
            a += 1
    if x==1:
        d["state"] = 'normal'
        d.delete(0.0, tk.END)
        for j in getData():

            d.insert("insert", msg[i])
            d.update()
            d["state"] = 'disabled'
    else:
        bt2 = tk.Button(window, text='更新', width=5, height=1, command=new)
        bt2.grid(row=4, column=int(len(getData())/2)+2, padx=20, pady=20)
        fun()


def new():
    begin(1)



def out():
    window.destroy()

    oo = os.getpid()
    import subprocess
    subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % oo, shell=True)

    # print(os.getpid())

def go():
    begin(0)

def mixed_action(btn):
    go()
    btn["state"] = 'disabled'

bt = tk.Button(window, text='启动', width=8, height=1)
bt.config(command = lambda: mixed_action(bt))
bt.grid(row=4, column=int(len(getData())/2)-2,padx=20, pady=20)



#bt2 = tk.BugetDataon(window, text='设置', width=5, height=1, command=config)
#bt2.grid(row=4, column=4, padx=20, pady=20)

window.protocol("WM_DELETE_WINDOW", out)

window.mainloop()
