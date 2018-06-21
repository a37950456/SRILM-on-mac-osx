#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:30:53 2018

@author: tinatsai
"""


zhuyin =['ㄅ','ㄆ','ㄇ','ㄈ','ㄉ','ㄊ','ㄋ','ㄌ','ㄍ','ㄎ','ㄏ','ㄐ','ㄑ','ㄒ','ㄓ',
         'ㄔ','ㄕ','ㄖ','ㄗ','ㄘ','ㄙ','ㄧ','ㄨ','ㄩ','ㄚ','ㄛ','ㄜ','ㄝ','ㄞ','ㄟ',
         'ㄠ','ㄡ','ㄢ','ㄣ','ㄤ','ㄥ','ㄦ']

words=[]
for i in range(0,len(zhuyin)):
    words.append([])
## Open file
uz = open('utf8-ZhuYin.map', "r",encoding = 'utf8') #r only read
for line in uz.readlines():
    line = line.strip().split(' ')
    first = line[0]
    two = line[1].split('/')
    for item in two:
        index = zhuyin.index(item[0])
        if(first not in words[index]):
            words[index].append(first)
uz.close()

zu = open('ZhuYin-utf8.map','w')   #w rewrite
for i in range(0,len(zhuyin)):
    line = ""
    for j in range(0,len(words[i])):
        line += words[i][j] + " "
    zu.write(zhuyin[i] + " " + line + "\n")
    for j in range(0,len(words[i])):
        zu.write(words[i][j] + " " + words[i][j] + "\n")
zu.close()


