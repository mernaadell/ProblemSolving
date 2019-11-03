#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 04:11:07 2019

@author: merna
"""

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])

    t = int(st[1])
    count2=0
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])
    count=0
    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    for i in  apples:
        i=i+a
        if i>=s and i<=t:
            count=count+1
      
    for j in  oranges:
        j=j+b
        if j>=s and j<=t:
            count2=count2+1
    print(count)
    print(count2)
