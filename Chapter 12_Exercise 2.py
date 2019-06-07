#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
count =0 
try:
    url = input("Enter a URL:\n")
    for urlparts in url:
        urlparts = url.split("/")
        host = urlparts[2]
    print("host: ", host,"\n")
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd0 = "GET {} HTTP/1.0\r\n\r\n".format(url)
    cmd = cmd0.encode()

    message = ""
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count = count+len(data)
        message = message + data.decode()
    
    if len(message)>3000:    
        info = (message[:3000] + '..')
        print(info)
    else:
        print(message)
    print("\nTotal characters: ",count)
    mysock.close()
except:
    print("bad URL")


# In[ ]:





# In[ ]:




