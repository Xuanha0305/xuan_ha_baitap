# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:31:02 2024

@author: Xuanha 
"""

import random
def generate_random_number(start, end):
    return random.randint(start, end)
# Ví dụ sử dụng
start = 10
end = 50
random_number = generate_random_number(start, end)
print(f"Số ngẫu nhiên trong khoảng từ {start} đến {end}: {random_number}")
