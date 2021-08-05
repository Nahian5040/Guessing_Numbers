'''This is a project where we have to guess a random number from 1 to 100 and the programme will show us 
if we guess right or wrong''' 
import time
import random
randNumber = random.randint(1,100)
guesses = 0
while True:
    userGuess = input("Enter your Guess from (1-100):")
    try:
        userGuess = int(userGuess)
    except Exception as e:
        print(f"Invalid input:{e}")
    else:
        if(userGuess == randNumber):
            print("You guessed it right!")
            break
        elif(userGuess != randNumber):        
            if(randNumber > userGuess):
                print("You are wrong! you write an smaller number")
            else:
                print("You are wrong! You write an bigger number")
    guesses += 1
    
print(f"You guessed the number in {guesses+1} gusses")
time.sleep(5)
           

