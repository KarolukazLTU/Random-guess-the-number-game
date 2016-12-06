import random
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv);

def clear():
    os.system('cls' if os.name=='nt' else 'clear');

name = input ("Hello, What is your name? ");
print("Welcome" , name , ", try and guess a number between 1 and 20 \n");

num = (random.randint (1,20));



while True:

  guess = int(input ("Your Guess: "));
  
  if guess < num :
    print("Too low: ");

  if guess > num :
    print("Too high: ");

  if guess == num :
    print("You've guessed it! It's" , num);
    exit();
    
restart = input("Do (y)ou want to play again? ");
if restart == "y":
    clear();
    restart_program();
else:
    exit();
