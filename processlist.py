#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:57:52 2018

@author: hans
"""

ReadTxt = 'list_attr_celeba.txt'
WriteTxt = 'train.txt'
r = open(ReadTxt,'r')
w = open(WriteTxt,'w')
rLine = r.readline().split('\n')[0]
while rLine:
    rLine = r.readline().split('\n')[0]
    if not rLine:
        break
#    image,bangs,eyeglasses,gender,
    wLine = rLine.split(' ')[0]+' '+rLine.split(' ')[6]+' '+rLine.split(' ')[16]+' '+rLine.split(' ')[21]+'\n'
    w.write(wLine)
r.close()
w.close()