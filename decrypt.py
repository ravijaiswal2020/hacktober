from cryptography.fernet import Fernet

plain_text = input("Enter a message to be encrypted: ")
# fernet key to generate to encrypt and decrypt
key = Fernet.generate_key()
# create a fernet object from Fernet class
fernet = Fernet(key)
cipehr_text = fernet.encrypt(plain_text.encode())
print("Original Message: ",plain_text)
print("Encrypted Message: ",cipehr_text)

decoded_text = fernet.decrypt(cipehr_text).decode()
print("Decrypted Message: ",decoded_text)
