#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:09:15 2019

@author: merna
"""

if __name__ == '__main__':
    count=0
    s = input()
    x=len(s)/3
    s2="SOS"
    j=0
    for i in range(len(s)):
        print(i," ",j)
        if j==3:
            j=0
        if s[i]!=s2[j] :
            count+=1
            j+=1
        else:
            j+=1
    print(count)
            
            
 