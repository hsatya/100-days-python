

def encoding(message, step):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encode = ""

    for m in message:
        if m in letters:
            i = letters.index(m)
            encode_by = i + step
            if encode_by > 25:
                diff = (encode_by) - 25
                encode += letters[diff - 1]
            else:
                encode += letters[encode_by]

        else:
            encode += m

    print(encode)

def decode(plain_text,  shift_amount):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = positioo + shift_amount

        if new_position< 0:
            new_position = new_position + 26

        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(cipher_text)

def ceaser_cipher(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    if new_position > 25:
      new_position = new_position - 26
    elif new_position < 0:
      new_position = new_position + 26
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}.")
    
message = input("Enter message to encode: ").lower()
step = int(input("Enter the step size: "))
encoding(message, step)

def encode(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    if new_position > 25:
      new_position = new_position - 26
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}.")

def decode(cipher_text, shift_amount):
  plain_text = ""
  
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount

    if new_position < 0:
      new_position = new_position + 26

    new_letter = alphabet[new_position]
    plain_text += new_letter
  
  print(f"The decoded text is {plain_text}.")
