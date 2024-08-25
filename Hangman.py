def prints_greeting():
    print("Are you ready to play Hangman? (Type 'Y' or 'N'")
    player_answer = input ("> ")
    player_answer = player_answer.upper()
    print("Let's find out what word is hidden.\n")
    
    print("I hope you like fruit! Have fun!\n")
    print()

    

import random  

words_options = ["banana", "apple", "watermelon", "mango", "pineapple"]
words_to_guess = random.choice(words_options) 
print(f"The word to guess has been selected. ")

chances = 4
win = False
player_guess = []

prints_greeting()


while True:
    for letter in words_to_guess:
        if letter in player_guess:
            print(letter, end=" ")
        else:
            print("_", end= " ")
    print(f"You have {chances} chances.")   
    print("")
    guess = input("Choose a letter: ")
    player_guess.append(guess)
    if guess not in words_to_guess:
        chances -= 1

    win = True
    for letter in words_to_guess:
        if letter not in player_guess:
            win = False

    if chances == 0 or win:
     break     
        
if win:
    print(f"You must be a fruit lover ;) \nYou've guessed the word correctly: {words_to_guess}.")
else:
    print(f"Uh Oh, You must not like {words_to_guess} you've run out of chances.")


