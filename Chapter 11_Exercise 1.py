#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
count = 0;
file = input("Enter filename ")
fhand = open(file)
rex = input("Enter regular expression ")
for line in fhand:
    line = line.rstrip()
    x = re.findall(rex, line)
    if len(x) > 0:
        count = count+1
print(file," had ",count," lines that matched ", rex)


# In[ ]:





# In[ ]:




