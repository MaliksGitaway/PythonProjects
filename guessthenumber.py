import random


print("Hello, whats your name?")
name = input()
print ("Good Evening "+name+",would you like to play a game? If so, please type yes. If not, please type no.")
answer = input()

play = "yes"
no = "no"

if answer == play:
    print("Please guess a number between 1 and 6.")
    guess = int(input())
    x = random.randint(1,6)
    print(x)
elif answer == no:
    print("Thank you for coming, maybe another time.")

while guess != x:
    if guess > x:
     print("guess too high, aim lower")
    if guess < x:
     print("guess too low, shoot higher")

    guess = int(input())

guess == x
print("Congrats, right on the money!")

