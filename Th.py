# -*- codeing = utf-8 -*-
# @Time : 2020/6/27 0027 10:19
# @Author : Zz
# @File : Th.PY
# @Software : PyCharm

import threading

import datetime

import pythoncom

from gtt import getTime
from Data import getData
from audio import saudi



def fun():
    #pythoncom.CoInitialize()
    a = rec()
    if a == 1:
        saudi()
    else:
        print(a)
    #pythoncom.CoUninitialize()

    timer = threading.Timer(60, fun)
    timer.start()


def rec():
    for i in getData():
        h, m = getTime(i)
        curr_time = datetime.datetime.now()+datetime.timedelta(seconds=-7)
        if curr_time.hour == h and curr_time.minute == m and i in getData():
            print("时间到" + str(datetime.datetime.now()))
            return 1
        print(i+str(curr_time))
    print("------------------------"+"\n")

    # pid = os.getpid()
    # print(str(a)+''+str(pid))
    # if a==3:
    #    stop_thread(timer)
    # os.kill()

    # print("时间到")


#fun()

'''
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)



def func1(a):
    #Do something
    print('Do something')
    a+=1
    print(a)
    print('当前线程数为{}'.format(threading.activeCount()))
    if a>100:
        return
    t=threading.Timer(5,func1,(a,))
    t.start()

func1(0)
'''
