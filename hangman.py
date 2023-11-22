import random


word_list = ["aardvark", "baboon", "camel"]

#index = random.randint(0,len(word_list)-1)
#chosen_word = word_list[index]

chosen_word = random.choice(word_list)


#blanks = ""
#for l in chosen_word:
#   blanks += "_"

word_length = len(chosen_word)
blanks = "_" * word_length

print(blanks)

lifes = 6
alphabets = list("abcdefghijklmnopqrstuvwxyz")


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
        

        if "_" not in blanks:
            print("You Win")
            break

    else:
        lifes -= 1
        print("Wrong Guess.")
        
    if lifes == 0:
        print("Game Over\nYou lost!")
        print(f"The word was: {chosen_word}")
    else:
        letter = input("Guess a letter: ").lower()
        while letter not in  alphabets:
            letter = input("The letter was already used please guess another letter: ").lower()

        alphabets.remove(letter)
