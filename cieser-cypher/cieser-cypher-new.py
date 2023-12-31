
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position > 25:
        new_position = new_position - 26
      elif new_position < 0:
        new_position = new_position + 26
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"The {cipher_direction}d text is {end_text}.")

should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
  again = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n") 
  if again != "yes":
    should_continue = False

print("🖐  GoodBye!")
