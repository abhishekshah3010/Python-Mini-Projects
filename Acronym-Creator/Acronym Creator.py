#!/usr/bin/env python
# coding: utf-8

# ## A python program that generates a short form of a word from a given sentence.

# In[1]:


user_input = str(input("Enter a Phrase: "))
text = user_input.split()
acronym = " "
for i in text:
    acronym = acronym + str(i[0]).upper()
print("The acronym is" + acronym)


# In[ ]:




