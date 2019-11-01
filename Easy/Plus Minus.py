#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:30:36 2019

@author: merna
"""
if __name__ == '__main__':
    n = int(input())
    p=0
    ne=0
    b=0
    arr = list(map(int, input().rstrip().split()))
    for i in range(len(arr)):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            ne+=1
        else:
            b+=1
    print(p/n,"\n",ne/n,"\n",b/n)
            
