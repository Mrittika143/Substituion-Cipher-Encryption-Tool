import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)
#print(f"Characters are:{characters}")
key = characters.copy()
random.shuffle(key)
#print(f"Keys are :{key}")

#ENCRYPT
def encrypt(plain_text):
    cipher_text = ""

    for letter in plain_text:
        if letter in characters:
            cipher_text += key[characters.index(letter)]
        else:
            print(f"Warning: Skipping unsupported character '{letter}'")
    return cipher_text

#DECRYPT
def decrypt(cipher_text):
    plain_text = ""

    for letter in cipher_text:
        if letter in key:
            plain_text += characters[key.index(letter)]
        else:
            print(f"Warning: Skipping unsupported character '{letter}'")
    return plain_text

#INTERACTION WITH USER
if __name__ == "__main__":
    print("Substituion Cipher Encryption Tool")

    while True:
        print("1.Encrypt a message")
        print("2.Decrypt a message")
        print("3.Exit")
        choice= input("Enter your choice : ")

        if choice == "1":
            message= input("Enter the message to be encrypted : ")
            encrypted_message= encrypt(message)
            print(f"The encrypted message is : {encrypted_message}")

        elif choice == "2":
            message = input("Enter the message to be decrypted : ")
            decrypted_message = decrypt(message)
            print(f"The decrypted message is : {decrypted_message}")

        elif choice == "3":
            print("Exiting the program")
            break
        else:
            print("Invalid choice!Please select 1,2 or 3.")
