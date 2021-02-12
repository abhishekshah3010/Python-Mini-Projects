#!/usr/bin/env python
# coding: utf-8

# In[1]:


values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


# In[2]:


roman_numeral = str(input("Enter any Roman Numeral: "))
sum = 0
for i in range(len(roman_numeral) - 1):
    left = roman_numeral[i]
    right = roman_numeral[i + 1]

    if values[left] < values[right]:
        sum = sum - values[left]
    else:
        sum = sum + values[left]
sum = sum + values[roman_numeral[-1]]

print('{} to decimal is {}'.format(roman_numeral, sum))

