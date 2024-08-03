import random

def Guess_number():
    attempt=int(input("how many attempt to win your game :"))
    rand_num=random.randint(1,10)
    player_name=input(" your good  name : ")
    print(f"Hi {player_name}")
    print("Enter the number between 1 and 10")
    for x in range(attempt):
       guess=int(input("your guess:"))
       if guess == rand_num:
        print("Nice! you got it")
        play_again()
        return
       elif guess < rand_num:
        print("The random number it higher your guess number")
       else :
         print("The random number it lower your guess number")

    print(f"Sorry you have used all {attempt}attempt.The number was {rand_num}")
    play_again()

def play_again():
  Again=input("would you like to play again ? Enter (yes/No)")
  if Again.lower()== "yes":
    Guess_number()
  else:
    print('That\'s cool, Thanks!')
    exit()

Guess_number()
play_again()

