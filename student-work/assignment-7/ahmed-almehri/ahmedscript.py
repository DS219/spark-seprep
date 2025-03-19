#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 17:01:28 2025

@author: ahmed
"""
def palindrome(x):
    string = str(x)
    reverse = string[::-1]
    return string == reverse

print("racecar is palindrome:", palindrome("racecar"))
print("hello is palindrome:", palindrome("hello"))