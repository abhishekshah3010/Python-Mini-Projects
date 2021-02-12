#!/usr/bin/env python
# coding: utf-8

# In[1]:


height = float(input("Enter your height in Centimeters(cms): "))
weight = float(input("Enter your Weight in Kilograms(kg): "))

height = height/100
bmi = weight/(height*height)
print("Your Body Mass Index(BMI) is: ",bmi)
print()
if(bmi>0):
    if(bmi<=16):
        print("Attention! You are severely Underweight")
    elif(bmi<=18.5):
        print("Eat a lot! You are underweight")
    elif(bmi<=25):
        print("Yayy! You are Healthy")
    elif(bmi<=30):
        print("You are overweight")
    else: print("Attention! You are severely overweight")
else:("Please enter valid details")

