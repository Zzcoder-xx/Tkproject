#-*- codeing = utf-8 -*-
#@Time : 2020/6/27 0027 10:56
#@Author : Zz
#@File : time.PY
#@Software : PyCharm

import json
import datetime
import dateutil.parser
import decimal
from Data import getData


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


def getTime(i):

    data = getData()

    thing = json.dumps(data, cls=MyJSONEncoder)

    a = json.loads(thing, object_hook=object_hook)

    y = a[i]

    #print(y)


    time = datetime.datetime.strptime(y, "%H:%M")
    #time = thing['thing']

    return time.hour,time.minute


#for i in Data.tt():
#    h,m=main(i)
#   print(h,m)

