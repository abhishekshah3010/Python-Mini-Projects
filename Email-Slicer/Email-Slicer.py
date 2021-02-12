#!/usr/bin/env python
# coding: utf-8

# In[1]:


user_input = str(input("Enter you email id: "))
username, domain = user_input.split('@')
print("Your username is: " + username)
print("Your domain is: " + domain)

