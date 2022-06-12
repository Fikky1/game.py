
import random

R= "rock"
P = "Paper" 
S = "Scissors"
alist = ["rock" ,"Paper","Scissors"]
print(R,P,S)
user_action = input ("Enter a choice(R, P, S): ")
possible_actions = ["rock" ,"paper","scissors",]
computer_action = random.choice(possible_actions)
print(f"\nPlayer{user_action}, computer{computer_action}.\n")
if user_action == computer_action:
     print(f"Both players selected{user_action}.it's a tie!")
elif user_action =="rock":
   if computer_action == "scissors":
     print("rock smashes scissors! you win!")
   else:
    print("paper covers rock! you lose")
elif user_action == "paper":
   if computer_action == "rock":
     print("Paper covers rock! you win!")
   else:
     print("Scissors cuts paper! you lose.")
elif user_action == "Scissors":
   if computer_action == "paper":
     print("Scissors cuts paper! you win")
   else:
     print("rock smashes scissors! you lose.")
     

     




    
