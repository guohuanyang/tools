# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         test
# Description:  
# Author:       guohuanyang
# Date:         2021/12/7
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------

import random
import time


start = time.time()
t = 0
while t < 1000:
    x = [random.randint(0, 255) for _ in range(256)]
    x_1 = [True if j>127 else False for j in x]
    t += 1
end = time.time()
print(end-start)

start = time.time()
t = 0
while t < 1000:
    y = [i for i in range(256)]
    y_1 = [True if k>127 else False for k in y]
    t += 1
end = time.time()
print(end-start)


