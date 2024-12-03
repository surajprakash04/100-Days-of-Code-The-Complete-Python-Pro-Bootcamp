import string

alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        cipher_text += alphabet[shift_position]
    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)

def decrypt(original_text, shift_amount):
    decipher_text = ""

    for letter in original_text:
        shift_position = alphabet.index(letter) - shift_amount
        shift_position %= len(alphabet)
        decipher_text += alphabet[shift_position]
    print(f"Here is the encoded result: {decipher_text}")

decrypt(original_text=text, shift_amount=shift)
