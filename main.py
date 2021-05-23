from art import logo
from random import randint

def guess(attempt,  level, computer):
  while(attempt != 0):
    print(f"You have {attempt} attempts remaining to guess the number.")
    num = int(input("Make a guess: "))
    if num == computer:
      print(f"You got it! The answer was {num}.")
      return
    elif num > computer:
      print("Too high.")
      attempt -= 1
    else:
      print("Too low.")
      attempt -= 1
    if attempt != 0:
      print("Guess again.")
  print("You've run out of guesses, you lose.")



def game_start():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  level = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
  if level == "easy":
    attempt = 10
  else:
    attempt = 5
  computer = randint(1, 100)
  guess(attempt, level, computer)

game_start()