#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:15:24 2019

@author: merna
"""
import math as m
if __name__ == '__main__':
    
    n = int(input().strip())
    arr = []
    sum=0;sum2=0
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(n):
        j=i
        sum+=arr[i][j]
    for i in range(n):
        j=n-i-1
        sum2+=arr[i][j]
    print(abs(sum2-sum))
        
    
         
