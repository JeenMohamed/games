import random

hangman0 = [
"""
+---+
  | |
  O | 
    | 
    ===""", """
+---+
  | |
  O | 
  | | 
    ===""", """
+---+
  | |
  O | 
 /| |
    ===""", """
+---+
  | |
  O | 
 /|\|
    ===""", """
+---+
  | |
  O | 
 /|\|
 /  ===""", """
+---+
  | |
  O | 
 /|\|
 / \ ===""", """
"""
]

FOOD = ['blueberry muffin','fudge','redvelvet','chocolate','gram crackers'] 
word = random.choice(FOOD).lower()
# 1 = len(word)
# for i in range (1):
#     print("_", end = " ")
GUESSED_RIGHT = []
GUESSED_WRONG = []
tries = 6
hangman_count = -1
while tries > 0:
    output = ''
    for letter in word:
        if letter in GUESSED_RIGHT:
            output += letter
        else:
            output += '_ ' 
    if output == word:
        break
    print("Guess the word correctly: ",output)
    print(tries," Chances left. Enter a letter to guess the word.")
    guess = input().lower()
    if guess in GUESSED_RIGHT or guess in GUESSED_WRONG:
          print("Already guessed", guess)
    elif guess in word : 
        print('Great, you guessed the letter correctly.')
        GUESSED_RIGHT.append(guess)
    else:
        print("Sorry, you guessed the letter incorrectly.")
        hangman_count = hangman_count + 1
        tries = tries - 1
        GUESSED_WRONG.append(guess)
        print(hangman0[hangman_count])
if tries > 0:
    print("you guessed the word, nice! YOU WON!")
else:
    print("Sorry, you didn't guess the word correctly. YOU LOST!")
