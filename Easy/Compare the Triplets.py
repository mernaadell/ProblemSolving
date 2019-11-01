# -*- coding: utf-8 -*-
import numpy as np

if __name__ == '__main__':
    alice=0;bob=0
    l =input().split()
    l2 = input().split()
    for i,j in zip(l,l2):
        print(i,j)
        if(i>j):
            alice=alice+1
        elif(i<j):
            bob=bob+1
    print(alice,bob)
        
        
        
