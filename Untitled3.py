#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q23


# In[6]:


def f(indent,pattern):
    if pattern==0:
        return
    else:
        print(""*indent + "*"*(pattern*2-1))
        f(indent+1, pattern -1)
        
f(0,0)
f(0,1)
f(0,2)
f(0,4)


# In[ ]:




