# -*- coding: utf-8 -*-
import numpy as np

# Complete the matchingStrings function below.
if __name__ == '__main__':
    
    x=int(input())
    l=[input() for i in range(x)]
    print(l) 
    y=int(input())
    l2=[input() for j in range(y)]
    print(l2) 
    answer=[]
    for k2 in l2:
        print(k2)
        answer.append(l.count(k2))
    for t in answer:
        print(t)
