#M03.PA - Realiseren

import random
import time

print("Welcome to the guessing game, this is your first round.\n " )
time.sleep(1)
print("There are 20 rounds, each round you have 10 guesses to guess the mystery number.\n ")
time.sleep(1)
print("If you guess the number on time, you earn a point, with 20 points  you win the game!\n ")
time.sleep(1)

rounds = 1
guesses = 0 
score = 0 

maxrounds = 21
maxguesses = 10

while rounds > 0 and rounds <= 21:
   number = random.randint(1, 1000)
   print(number)

   while True: # while van maken anders gaat hij 10 keer raden ook als je het al hebt

      guess = int(input("Which number do you think it is? \n ")) 
      difference = number - guess
      rounds = rounds + 1
   
      if guess > number: 
         print("Lower! \n")
         guesses = guesses + 1
      elif guess < number:
         print("Higher! \n")
         guesses = guesses + 1
      elif guess == number: # onderaan 
         print("You've guesses it! \n") 
         score = score + 1
         guesses = guesses + 1
      elif difference < 20 or difference < -20 :
         print("You're very close! \n")
      elif difference > 20 and difference < 50 or difference > -20 and difference < -50:
         print("You're extremely close to the number! \n")
      if guess == number or guesses == maxguesses:
         print("New round!")
         print(f"You have {score} points right now!\n ")
         break
   if rounds == maxrounds:
      if score == 20:
         print(f"Congrats, you won with {score} points!")
      else:
         print(f"Game over! You have {score} points!")
      break
