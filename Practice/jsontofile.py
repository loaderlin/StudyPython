#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import codecs

def jsontofile():
    mydict = [{
        'name': '賴小七',
        'age': 20,
        'qq': 123456,
        'friends': ['娟妹', '。。。'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    },
    {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    ]
    try:
        with codecs.open('data.json', 'w', encoding='utf-8') as fs:
            # 这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
            # [ensure_ascii=False 参考链接](https://www.cnblogs.com/stubborn412/p/3818423.html)
            json.dump(mydict, fs, ensure_ascii=False)
    except IOError as e:
        pass
    finally:
        if fs:
            fs.close()
            
if __name__ == '__main__':
    jsontofile()
