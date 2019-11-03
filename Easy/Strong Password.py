#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 00:39:15 2019

@author: merna
"""
import re 
if __name__ == '__main__':
    n = int(input())
    password = input()
    # Make own character set and pass  
    # this as argument in compile method 
    count=0
    flag=1
   
    
    regex = re.compile('[!@#$%^&*()-+-]') 
    if(regex.search(password) == None ): 
        count+=1
       
    regex = re.compile('[0123456789]')      
    if(regex.search(password) == None ): 
        count+=1 
       
    regex = re.compile('[abcdefghijklmnopqrstuvwxyz]')   
    if(regex.search(password) == None ): 
        count+=1
        
    regex = re.compile('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]') 
    if(regex.search(password) == None ): 
        count+=1
        
    if len(password)<6:
        if len(password)+count<6:
            count=count+(6-(len(password)+count))
            
    print(count)