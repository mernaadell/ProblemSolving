#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 01:50:26 2019

@author: merna
"""


import numpy 

if __name__ == '__main__':
    n = int(input())
    j=1
    count=0
    arr = list(map(int, input().rstrip().split()))
    for j in range(n):
        key=arr[j]
        i=j-1
        while i>=0 and key<arr[i]:
            arr[i+1]=arr[i]
            count=count+1
            i=i-1
        arr[i+1]=key
       
    print(count)
        
        
        