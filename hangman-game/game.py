import random
from words import word_list
from arts import logo, stages

chosen_word = random.choice(word_list)

word_length = len(chosen_word)
blanks = "_" * word_length
print(logo)
print(blanks)

lifes = len(stages) - 1
end_of_game = False

while not end_of_game:
    letter = input("Guess a letter: ").lower()
    print(letter)
    if letter in chosen_word:
      blanks = list(blanks)

      for position in range(word_length):
          if letter == chosen_word[position]:
              blanks[position] = letter
      blanks = "".join(blanks)

      print(blanks)
      if "_" not in blanks:
        end_of_game = True
        print("You Win.")
    else:
      lifes -= 1
    print(stages[lifes])

    if lifes < 1:
      end_of_game = True
      print("You Lose.")

