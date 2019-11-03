#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:41:02 2019

@author: merna
"""

if __name__ == '__main__':
    count=0 
    s = input()
    if s[0].isupper():
        count=0
    else:
        count=1
  
    for i in s:
        if i.isupper():
            count+=1
    print(count)
            