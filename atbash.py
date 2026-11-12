# atbash.py
# @author Roberto Travers (25108433)

# Declare the letters of the alphabet, both in order and reversed 
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_reverse = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

# Declare the function for atbash encryption
def atbash_encrypt(message):

    # Declare variables for the encrypted message
    message_encrypted = ""

    # Create a for loop to handle the actual process of encryption
    for letter in message:
        if letter.upper() in alphabet:
            position = alphabet.index(letter.upper())
            message_encrypted += alphabet_reverse[position]
        else:
            message_encrypted += letter

    # Return the encrypted message at the end of the for loop
    return message_encrypted

# Declare function for atbash decryption
def atbash_decrypt(message):
    # Declare empty string for the decrypted message
    message_decrypted = ""

    # Create for loop to handle process of decryption. Essentially works the same as the one above, but working in reverse.
    for letter in message:
        if letter.upper() in alphabet_reverse:
            position = alphabet_reverse.index(letter.upper())
            message_decrypted += alphabet[position]
        else:
            message_decrypted += letter

    # Return the decrypted message at the end of the for loop
    return message_decrypted

# Take user input for the initial message and their choice of encryption or decryption
message = input("Please enter your message: ")
choice = input("\nWould you like to encrypt or decrypt the provided message? Please enter: \n1 for Encryption \n2 for Decryption \nYour choice: ")

# Basic if-else statement to decide which functions to call on depending on the user's choice
if choice == "1":
    encryption_result = atbash_encrypt(message)
    print("Encrypted message:", encryption_result)
elif choice == "2":
    decryption_result = atbash_decrypt(message)
    print("Decrypted message:", decryption_result)
else:
    print("Invalid input. Please restart.")
