import string
import art

print(art.logo)

alphabet = list(string.ascii_lowercase)

def caesar(original_text, shift_amount, encode_decode):
    output_text = ""

    if encode_decode == "decode":
            shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shift_position = alphabet.index(letter) + shift_amount
            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]
        else:
             output_text += letter
    print(f"Here is the {encode_decode}d result: {output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
         should_continue = False
         print("Goodbye!")
         