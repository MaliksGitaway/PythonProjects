import random


answer1 = input("Wanna play rock, paper, scissors?")
game = ["rock", "paper", "scissors" ]
game1 = ["paper" , "scissors"]
game2 = ["rock" , "scissors"]
game3 = ["paper" , "rock"]

answer2 = input("Make your selection foe!")

if answer1 == "yes" or "y":
    if answer2 == "rock":
     print(random.choice(game1))
     print("Thanks for playing!")
    if answer2 == "paper":
      print(random.choice(game2))
      print("Thanks for playing!")
    if answer2 == "scissors":
     print(random.choice(game3))
     print("Thanks for playing!")