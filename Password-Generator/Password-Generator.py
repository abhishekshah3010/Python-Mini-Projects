#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


password_length = int(input("Enter the length of the password you want: "))
password_string = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"
password = "".join(random.sample(password_string, password_length))
print(f"Password: {password}")

