#!/usr/bin/env python
# coding: utf-8

# In[1]:


def quiz(question, answer):
    global score
    guessing = True
    attempt = 0
    while guessing and attempt < 3:
        if question.lower() == answer.lower():
            print("Correct Answer")
            score+=1
            guessing = False
        else:
            if attempt < 2:
                question = input("Sorry Wrong Answer! Please try again")
            attempt+=1
    if attempt == 3:
        print("Nevermind! The Correct answer is ",answer )


# In[2]:


score = 0
print("Guess the Animal")


# In[3]:


question1 = input("Which is the National Bird of India? ")
quiz(question1, "Peacock")

question2 = input("Which is the fastest land animal? ")
quiz(question2, "Cheetah")

question3= input("Which is the tallest living animal? ")
quiz(question3, "Giraffe")

question4 = input("Which is the larget living bird? ")
quiz(question4, "Ostrich")

question5 = input("Which is the larget living animal? ")
quiz(question5, "Blue Whale")

question6= input("Which is the largest of all lizards? ")
quiz(question6, "Komodo Dragon")

print("Your Score is "+ str(score))


# In[ ]:




