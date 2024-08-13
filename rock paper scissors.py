#here we are buliding a simple rock paper scissors game
#to build it we are going to use the rndom module so that can make random choices among rock paper and scissors

import random

def play():
    
    u_choice=input("please choose amongst 'r'','p',or 's': ")
    c_choice=random.choice(['r','p','s'])
    
    if u_choice=='r' and c_choice=='r':
        print("it is a tie!")
    
    if u_choice=='r' and c_choice=='p':
        print("oops! the computer chose paper")
    
    if u_choice=='r' and c_choice=='s':
        print("yayy! you won")
    
    if u_choice=='p' and c_choice=='r':
        print("yayy! you won")
    
    if u_choice=='p' and c_choice=='p':
        print("it is a tie!")
    
    if u_choice=='p' and c_choice=='s':
        print("oops! the computer chose scissors")
    
    if u_choice=='s' and c_choice=='r':
        print("oops the computer chose rock!")
    
    if u_choice=='s' and c_choice=='p':
        print("yayy! you won")
     
    if u_choice=='s' and c_choice=='s':
        print("it is a tie!")
    

play()