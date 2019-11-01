#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:42:32 2019

@author: merna
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):  
        print(' ' * (n-i)+"#"*i)
           
       