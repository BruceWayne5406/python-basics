s_word="engineer"
guess_count=0
guess=""

while guess_count<3:
    guess_count=guess_count+1
    guess=input("enter your guess: ")
    if guess==s_word:
        print("you won! ")

if guess!= s_word and guess_count==3:
 
    print("you couldnt guess the correct word ")