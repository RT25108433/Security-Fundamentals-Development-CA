# Caesar Cipher
# Aaron Bridger
# 24247421


# Will shift each letter by a chosen number in the alphabet.
def encrypt(text, shift):
    result = ""

    # Go through the message one character at a time
    for char in text:
        if char.isalpha():
            # Keep uppercase and lowercase letters working correctly
            start = ord("A") if char.isupper() else ord("a")

            # Shift the letter and wrap around after Z
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Keep spaces, numbers and punctuation unchanged
            result += char

    return result

# Decrypting is just the opposite of encrypting
def decrypt(text, shift):
    # Decryption shifts the letters in the opposite direction
    return encrypt(text, -shift)


# Simple test so the file can be run on its own
message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
choice = input("Encrypt or decrypt? ").lower()


if choice == "encrypt":
    result = encrypt(message, shift)
else:
    result = decrypt(message, shift)

print("Result:", result)