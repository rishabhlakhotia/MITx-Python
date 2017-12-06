# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:04:25 2016

@author: Rishabh Lakhotia
"""
s = "azcbobobegghakl"
count = 0

vowels = 'bob'

for x in range(len(s)):
    if s[x:x+3] in vowels:
        count += 1;
        
print("the number of times bob appears = " + str(count))