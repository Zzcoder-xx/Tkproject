# -*- codeing = utf-8 -*-
# @Time : 2020/6/27 0027 0:12
# @Author : Zz
# @File : audio.PY
# @Software : PyCharm


import pyttsx3
import datetime


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

    engine.runAndWait()
