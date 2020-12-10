#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:39:41 2020

@author: 
"""
class Solution(object):
    def isValid(self, s):
        bstr=[]
        for i in s:
            if bstr==[]:
                bstr.append(i)
            elif i==')':
                if bstr[-1]=='(':
                    bstr.pop();
                else:
                    bstr.append(i)
            elif i==']':
                if bstr[-1]=='[':
                    bstr.pop();
                else:
                    bstr.append(i)
            elif i=='}':
                if bstr[-1]=='{':
                    bstr.pop();
                else:
                    bstr.append(i)
            else:
                bstr.append(i)
        if bstr==[]: 
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        
