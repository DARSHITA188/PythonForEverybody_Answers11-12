#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
count = 0;
total = 0;
avg = 0
file = input("Enter filename ")
fhand = open(file)
for line in fhand:
    line = line.rstrip()
    
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        number = int(x[0])
        total = total+number
        count = count+1
average = total/count
print(average)
        
        
        


# In[ ]:




