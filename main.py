alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(final_text, shift, direction):
  initial_text = ""
  if direction == "decode":
    shift *= -1
  for char in final_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      initial_text += alphabet[new_position]
    else:
      initial_text += char
  print(f"Here's the {direction}d result: {initial_text}")

from art import logo
print(logo)

flag = False
while not flag:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(final_text=text, shift=shift, direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    flag = True
    print("Thank you")
    


