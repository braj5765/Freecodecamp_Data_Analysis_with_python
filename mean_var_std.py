#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
def calculate(n):
    if len(n)!=9:
        raise ValueError('List should have 9 numbers')
    val=np.reshape(np.array(n),(3,3))
    cal={}
    cal['mean']=[np.mean(val,axis=0).tolist(), np.mean(val,axis=1).tolist(),np.mean(val.flatten()).tolist()]
    cal['variance']= [np.var(val,axis=0).tolist(), np.var(val,axis=1).tolist(),np.var(val.flatten()).tolist()]
    cal['standard deviation']= [np.std(val,axis=0).tolist(), np.std(val,axis=1).tolist(),np.std(val.flatten()).tolist()]
    cal['max']= [np.max(val,axis=0).tolist(), np.max(val,axis=1).tolist(),np.max(val.flatten()).tolist()]
    cal['min']= [np.min(val,axis=0).tolist(), np.min(val,axis=1).tolist(),np.min(val.flatten()).tolist()]
    cal['sum']=[np.sum(val,axis=0).tolist(), np.sum(val,axis=1).tolist(),np.sum(val.flatten()).tolist()]
    return cal


# In[ ]:





# In[ ]:




