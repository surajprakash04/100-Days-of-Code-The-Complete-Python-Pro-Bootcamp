import string

alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    letterIndex = []
    for letter in text:
        letterIndex.append(alphabet.index(letter))
        # move = letterIndex + shift
        # newAlpha = alphabet[move]
    print(letterIndex)

    newletterIndex = []
    for ele in letterIndex:
        newletterIndex.append((ele + shift)%len(alphabet))
    print(newletterIndex)

    outputText = ""
    for elem in newletterIndex:
        outputText += alphabet[elem]
    print(outputText)
elif direction == 'decode':
    letterIndex = []
    for letter in text:
        letterIndex.append(alphabet.index(letter))
        # move = letterIndex + shift
        # newAlpha = alphabet[move]
    print(letterIndex)

    newletterIndex = []
    for ele in letterIndex:
        newletterIndex.append((ele - shift)%len(alphabet))
    print(newletterIndex)

    outputText = ""
    for elem in newletterIndex:
        outputText += alphabet[elem]
    print(outputText)
    