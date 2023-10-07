import random
import string
# characters to be encrypted 0123456789abcdefghijklmnopqrstuvwxyz
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars : {chars}")
# print(f"Key : {key}")

# ENCTYPT
plain_text = input("Enter a message: ")
cipher_text = " "

for i in plain_text: # iterating through each string in the message
    index = chars.index(i) # taking out index from chars list
    cipher_text += key[index]
    
print(f"Original Message: {plain_text} ")
print(f"Encrypted Message: {cipher_text} ")
