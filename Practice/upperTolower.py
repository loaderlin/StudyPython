#!/usr/bin/env python
# coding=utf-8

def strupertolower():
    with open('gas.sql', 'w+') as fs :
        with open('GAS_DEV.sql', 'r+') as f :
            for line in f.readlines():
                fs.write(line.lower())


if __name__ == "__main__":
    strupertolower()
