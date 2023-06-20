import art
import random
import os

def check(comp_choice, player_choice):
    if player_choice > comp_choice:
        return 0
    elif player_choice < comp_choice:
        return 1
    else:
        return 2

def display_winner(last, number):
    
    print(f"THE NUMBER WAS {number}")
    
    if last:
        print(art.win)
    else:
        print(art.lose)
    
def game_mode():
    mode = input("Enter the mode of difficulty 'easy' or 'hard'\n")
    
    if mode == "easy":
        return 10
    else:
        return 5
    
    
def guess_number():
    
    print(art.logo)
    print("I'm thinking of a number from 1-100")


    lives = game_mode() 
    print(f"You have {lives} attempts to guess the number, Good Luck!")   
    comp_choice = random.randint(1,101)
    player_choice = 0
    win_lose = False


    while player_choice != comp_choice and lives != 0:
        player_choice = int(input("Make a guess: "))
        
        i = check(comp_choice, player_choice)
        
        
        if i == 2:
            win_lose = True
        elif i == 0:
            lives-=1
            print(f"Current attempts remaining = {lives}")
            print("Too High!")
        else:
            lives-=1
            print(f"Current attempts remaining = {lives}")
            print("Too Low!")


    display_winner(win_lose, comp_choice)
    
    
while( input("Do you want to play Guess The Number? y/n\n") == "y"):
    os.system('cls||clear')
    guess_number()