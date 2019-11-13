#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:12:20 2019

@author: merna
"""

if __name__ == '__main__':
    q = int(input())
    h="hackerrank"
    
    for q_itr in range(q):
        s = input()
        i=0
        j=0
            
           
        for i in range(len(s)):
            
           
            if s[i]==h[j] and j<=len(h):
               
                j=j+1
            if (j==len(h)):
                break
        if (j==len(h)):
               print("YES")
               
        else:
            print("NO")
            
                
                    
                
                
            
        
        
        