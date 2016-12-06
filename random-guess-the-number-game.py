import random
import sys
import os

def restart_program():
    python = sys.executable;
    os.execl(python, python, * sys.argv);

def clear():
    os.system('cls' if os.name=='nt' else 'clear');


def restart():
    restart = input("Do you want to play again? ");
    if restart == "yes":
        clear();
        restart_program();
    else:
        exit();

def randomnumber():
    
    num = (random.randint (1,20));

    print("Guess a number between 1 and 20!");
    
    while True:
    
      guess = int(input ("Your Guess: "));
      
      if guess < num :
        print("Too low: ");

      if guess > num :
        print("Too high: ");

      if guess == num :
        print("You've guessed it! It's" , num);
        restart();

def rps():
    
    r= ["Rock", "Paper", "Scissors"]
     
    computer = r[random.randint(0,2)]
    
    player = False
     
    while player == False:
        player = input("Rock, Paper, Scissors?: ");
        if player == computer:
            print("Tie!");
            restart();
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player);
                restart();
            else:
                print("You win!", player, "smashes", computer);
                restart();
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player);
                restart();
            else:
                print("You win!", player, "covers", computer);
                restart();
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player);
                restart()
            else:
                print("You win!", player, "cut", computer);
                restart();
        else:
            print("That's not a valid play. Check your spelling!");
        player = False
        computer = r[random.randint(0,2)];

    
name = input ("Hello, What is your name? ");

game = input("Hello! {0}, rps or num?: ".format(name));

if game == "num":
    
    randomnumber();

if game == "rps":

    rps();

