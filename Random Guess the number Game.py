#Karolis J
#07/12/15
#Random Module
import random

print ("Hello, What is your name?")
name = input ()
print("Welcome" , name , ", try and guess a number between 1 and 20")
guessestaken = 1

num = (random.randint (1,20))

while True:

    guess = int(input ("Your Guess:"))

    if guess <num :
        print("too low")

    if guess >num : 
         print("too high")

    if guess == num :
        print("You've guessed it! It's" , num)
        break
        
        


