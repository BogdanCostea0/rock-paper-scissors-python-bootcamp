# Rock paper scissors game
import random as r
print("Welcome to the rock paper scissors game")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ans = int(input("What you chose? 0 = rock , 1=paper, 2=scissors"))
if ans == 0:
    print("You chose:", rock)
elif ans == 1:
    print("You chose:", paper)
elif ans == 2:
    print("You chose:", scissors)
else:
    print("Not a good number. try again:")
    ans = int(input("What you chose? 0 = rock , 1=paper, 2=scissors"))

bot_ans = r.randint(0, 2)
if bot_ans == 0:
    print("Bot chose:", rock)
elif bot_ans == 1:
    print("Bot chose:", paper)
elif bot_ans == 2:
    print("Bot chose:", scissors)

if ans == 0 and bot_ans == 2:
    print("You win")
elif ans == 1 and bot_ans == 0:
    print("You win")
elif ans == 2 and bot_ans == 1:
    print("You win")
elif ans == bot_ans:
    print("Tie")
else:
    print("Bot wins")

