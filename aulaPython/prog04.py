#!/usr/bin/python3

import time

def funcao(msg, num):
    for i in range (num):
        print (msg)
        time.sleep(.5)

funcao ("primeira", 2)
funcao ("segunda", 7)
funcao ("terceira", 10)