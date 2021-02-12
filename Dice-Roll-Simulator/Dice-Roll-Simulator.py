#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


min_val = 1
max_val = 6


# In[3]:


roll_again = str(input("Do you want to roll the dice? "))
while roll_again == "yes" or roll_again == "Yes":
    print("Rolling The Dices...")
    print("The Values are :")
    print(random.randint(min_val, max_val))    
    print(random.randint(min_val, max_val))
    roll_again = input("Roll the Dices Again?") 

