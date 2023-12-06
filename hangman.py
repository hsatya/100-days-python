"""
import requests


chosen_word = ""
api_url = 'https://api.api-ninjas.com/v1/randomword'
response = requests.get(api_url,  headers={'X-Api-Key': 'vCiABjJW3cc5iMa97Hgs8g==SE7IWgMlu1Q5wuQH'})
if response.status_code == requests.codes.ok:
    data = response.text
    data = eval(data)
    chosen_word = data['word']
else:
    print("Error:", response.status_code, response.text)
"""
import random


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
blanks = "_" * word_length

print(blanks)


alphabets = list("abcdefghijklmnopqrstuvwxyz")

#################Stages##################
stages = ["""
    +---+
     |      |
    O     |
  / | \   |
  /   \   |
            |
=======
""", """
    +---+
     |      |
    O     |
  / | \   |
  /        |
            |
=======
""", """
    +---+
     |      |
    O     |
  / | \   |
            |
            |
=======
""", """
    +---+
     |      |
    O     |
  / |      |
            |
            |
=======
""", """
    +---+
     |      |
    O     |
     |      |
            |
            |
=======
""", """
    +---+
     |      |
    O     |
            |
            |
            |
=======
"""]


lifes = len(stages)
#################Asking User for Input##################
letter = input("Guess a letter: ").lower()
alphabets.remove(letter)

print(letter)


while lifes > 0:
    if letter in chosen_word:
        blanks = list(blanks)
        
        for position in range(word_length):
            if letter == chosen_word[position]:
                blanks[position] = letter
        blanks = "".join(blanks)

        print(blanks)

        if "_" not in blanks:
            print("You Win")
            break

    else:
        lifes -= 1
        print(stages[lifes])
        
    if lifes == 0:
        print("Game Over\nYou lost!")
        print(f"The word was: {chosen_word}")
    else:
        letter = input("Guess a letter: ").lower()
        while letter not in  alphabets:
            letter = input("The letter was already used please guess another letter: ").lower()

        alphabets.remove(letter)
