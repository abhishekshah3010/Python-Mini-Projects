#!/usr/bin/env python
# coding: utf-8

# # Fahrenheit to Celsius

# In[1]:


tempf = float(input("Enter the temperature in Fahrenheit: "))
tempc = (tempf - 32) * 5/9
print()
print(f'{tempf} Fahrenheit in Celsius is {round(tempc,2)}')


# # Celsius to Fahrenheit

# In[2]:


tempc = float(input("Enter the temperature in Celsius: "))
tempf = (tempc * 9/5) + 32
print()
print(f'{tempc} Celsius in Fahrenheit is {round(tempf,2)}')

