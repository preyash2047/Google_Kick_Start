#!/usr/bin/env python
# coding: utf-8

# Input<br>
# 3
# <br>4 100
# <br>20 90 40 90
# <br>4 50
# <br>30 30 10 10
# <br>3 300
# <br>999 999 999
# <br>
# 
# Output:<br>
# Case #1: 2
# <br>Case #2: 3
# <br>Case #3: 0

# In[3]:


sorted([20,90,40,90], reverse = False)


# In[1]:


T = int(input())
for x in range(1, T + 1):
    N, B = map(int, input().split())
    A = map(int, input().split())
    A = sorted(A, reverse = False)
    
    y = 0
    SUM = 0
    for i in range(0, N):
        SUM += A[i] 
        if SUM <= B:
            y += 1
        else:
            break
    print("Case #{}: {}".format(x, y), flush = True)

