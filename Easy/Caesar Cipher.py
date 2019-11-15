#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:33:49 2019

@author: merna
"""
from collections import deque
if __name__ == '__main__':

    n = int(input())

    s = input()

    k = int(input())
    st=""
    
    Original_alphabet="abcdefghijklmnopqrstuvwxyz"
    #items = deque(Original_alphabet)
    #items.rotate(k)
    #print(items)
    x=Original_alphabet[k:]+Original_alphabet[:k]
    y=x.upper()
    print(ord('a'))
    print(x)
    for i in s:
        if i.isalpha():
            if i.isupper():
                print(ord(i)-ord('A'))
                st+=y[ord(i)-ord('A')]
            else:
                print(ord(i)-ord('a'))
                st+=x[ord(i)-ord('a')]
        else:
            st+=i
    print(st)
   # for iin range()
    