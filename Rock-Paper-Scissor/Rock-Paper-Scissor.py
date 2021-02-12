#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


choices = ["Rock", "Paper", "Scissor"]
cpu_score = 0
player_score = 0


# In[3]:


while True:
    player = input("Rock, Paper or  Scissor?").capitalize()
    computer = random.choice(choices)
    
    if player == computer:
        print("Tie!")
        
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
            
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
            
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
            
    elif player=='End':
        print()
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        print()
        if cpu_score>player_score:
            print("Sad! CPU Wins")
        elif cpu_score==player_score:
            print("Phew! It's a Tie")
        else:
            print("Congrats! Player Wins")
        break


# In[ ]:




