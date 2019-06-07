#!/usr/bin/env python
# coding: utf-8

# In[2]:


try:
    import urllib.request, urllib.parse, urllib.error
    url = input("Enter URL :")
    fhand = urllib.request.urlopen(url)
    counts = 0
    li = []
    for line in fhand:
        words = line.decode()
        li.append(words)
        counts = counts+len(words)
    li = "".join(li)
    print("\n")
    print(li[:3000])

    print("\nTotal no of characters: ", counts)
except:
    print("bad url")
        
    
        


# In[ ]:





# In[ ]:




