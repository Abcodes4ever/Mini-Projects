import time
import sys
import random

def intro(firsttime):
    if firsttime:
        print("\nWelcome to the Random No. Guessing Game!")
        print("I will choose a number from 1 to 100. \nYou will have 5 chances to correctly guess the no. .\nIf you guess the number correctly within the given chances, you win.\nOtherwise, I win and you lose.")
        time.sleep(5)
        ans = input("Are you ready to play?(y/n) ")
    else:
        ans = input("Do you want to play again?(y/n) ")
    return ans

# Game mechanics    
def game():
    win_stat = False
    target = random.randint(1,100)
    time.sleep(2)
    print("\nThe number has been chosen.\nMay the guessing begin!")
    for i in range(5):
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

# Application
def app():
    # This ain't working, the value of "first" changed inside if ain't reflecting outside
    first = True
    if first:
        user_ans = intro(True)
        global first
        first = False
    else:
        intro(False)
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
    
        
