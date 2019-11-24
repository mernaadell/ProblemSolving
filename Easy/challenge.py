#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:01:10 2019

@author: merna
"""

if __name__ == '__main__':
    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(arr.index(V))