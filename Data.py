# -*- codeing = utf-8 -*-
# @Time : 2020/6/27 0027 0:02
# @Author : Zz
# @File : Data.PY
# @Software : PyCharm
import json



def getData():
    with open("config.json",encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
    return config

# a = getdata()
# for i in getdata():
#  print(a[i])

# for i in getdata():
#    h,m=gtt.main(i)
#    print(h,m)
