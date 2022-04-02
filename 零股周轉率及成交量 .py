#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import locale
a = []
b = []
aa = []
with open('odd_summary_1101227.csv', encoding='big5' , errors = 'ignore') as a1:
    rows = csv.reader(a1, delimiter=',')
    a += rows
    for j in range(3,886):
        errors = 'ignore'
        if a[j][3].replace(',','') =='----' or locale.atof(a[j][3].replace(',','')) =='----' :
            print('wrong')
        elif  float(a[j][3].replace(',',"")) >= 500:
            aa.append(a[j][1])
with open('STK_TURN_W_1101227.csv', encoding='big5' , errors = 'ignore') as a2:
    rows1 = csv.reader(a2, delimiter=',')
    b += rows1
    for j in range(3,90):
        for i in aa:
            if b[j][2] == i:
                print('一樣',b[j][1],b[j][2])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




