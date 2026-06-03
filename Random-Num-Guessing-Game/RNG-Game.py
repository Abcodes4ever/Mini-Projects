import time
import sys
import random

def intro():
    print("\nWelcome to the Random No. Guessing Game!")
    print("I will choose a number from 1 to 100. \nYou will have 3 chances to correctly guess the no. .\nIf you guess the number correctly within the given chances, you win.\nOtherwise, I win and you lose.")
    time.sleep(5)
    ans = input("Are you ready to play?(y/n)")
    return ans
    
def game():
    win_stat = False
    target = random.randint(1,100)
    time.sleep(2)
    print("\nThe number has been chosen.\nMay the guessing begin!")
    for i in range(3):
        user_num = int(input("Enter no.:"))
        if user_num == target:
            print("Correct!")
            win_stat = True
            break
        elif user_num > target:
            print("Too high!")
        elif user_num < target:
            print("Too low!")
    return win_stat, target



def exit_game():
    print("\nThanks for playing!")
    sys.exit(0)

    
def app():
    user_ans = intro()
    if user_ans.lower() == 'y':
        win, target = game()
    else:
        exit_game()
    if win:
        print("Congratulations!")
    else:
        print("Better luck next time!")
        print(f"The no. was: {target}")

while True:
    app()
    
        