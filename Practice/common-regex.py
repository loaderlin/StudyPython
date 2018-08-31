#!/usr/bin/env python
# coding=utf-8

import re

def main():
    input_str = "";
    m_username = re.match(r'^[0-9a-zA-Z_]{6,20}$', input_str)
    m_qq = re.match(r'^[1-9]\d{4,11}$', input_str)  
    # 使用了前瞻和回顾来保证手机号前后不应该出现数字
    m_iphone = re.match(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)', input_str)
    m_email = re.match(r'^[0-9a-zA-Z_-]+@[0-9a-zA-Z_-]+(\.[a-zA-Z0-9_-]+)+$', input_str)
    m_telephone = re.match(r'(\(\d{3,4}\)|\d{3,4}-)?\d{7,8}$', input_str)

    m_purified = re.sub(r'fuck|shit', "*", input_str, flags=re.IGNORECASE)
    m_sentence_list = re.split(r'[，。,.]', input_str) 
    while True:
        input_str = input('请输入\n ')
        input_str_match = re.match('',input_str)
        if not input_str_match:
            print('请输入有效\n')
        else:
            print ('成功匹配')
            break


def regex_iphone():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

if __name__ == '__main__':
    main()
    # regex_iphone()