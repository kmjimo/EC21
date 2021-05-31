#!/usr/bin/env python
# coding: utf-8

# In[15]:


import math
a=[]
for i in range(2,101):
    flag=0
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        a.append(i)
print(a)
a.reverse()
print(a)
b=[]
c=[]
for i in a:
    if(sum(b)<=sum(c)):
        b.append(i)
    else:
        c.append(i)
print(b)
print(sum(b))
print(c)
print(sum(c))


# In[ ]:




