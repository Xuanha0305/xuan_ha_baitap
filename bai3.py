# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:37:48 2024

@author: Xuanha 
"""

N=int(input("nhập số có 2 chữ số "))
if N>=10 and N<=99: 
    print("kết quả ", N%10+N//10 )
else:
    print("không hợp lệ ")
