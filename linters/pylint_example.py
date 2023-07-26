import string

shift = 3
choice = input("would you like to encode or decode?")
word = input("Please enter text")
letters = string.ascii_letters + string.punctuation + string.digits
ENCODED = ""
if choice == "encode":
    for letter in word:
        if letter == " ":
            ENCODED = ENCODED + " "
        else:
            x = letters.index(letter) + shift
            ENCODED = ENCODED + letters[x]
if choice == "decode":
    for letter in word:
        if letter == " ":
            ENCODED = ENCODED + " "
        else:
            x = letters.index(letter) - shift
            ENCODED = ENCODED + letters[x]

print(ENCODED)
