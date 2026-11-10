# Vigenere Cipher
# Author: Tony Nicoletti
# ID: 24210391

# The 26 letters the cipher works with. Each letter position (A=0, ... Z=25)
# is the number used in the Vigenere table.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Build the Vigenere table: 26 rows, each one that alphabet
# shifted one place further left than the row above it.
# alphabet[x:] thakes the letters from postition x to the end,
# alphabet[:x] take the letters before postition x.
# joining them wraps the start of the alphabet round to the end.
# Row 0 = ABC...Z, Row 1 = BCD...ZA, Row 2 = CDE...ZAB etc.
table = []
for x in range(26):
    table.append(alphabet[x:] + alphabet[:x])  # [x:][:x] is where to slice
    # Creates the Vigenere table.


def main():
    # Setting up the message, key, and mode for encryption or decryption.
    myMessage = """Bonnie was the best dog."""
    myKey = "BONNIENICO"
    myMode = "encrypt"  # encrypt or decrypt.

    # Call the matching function based on the mode selected.
    if myMode == "encrypt":
        translated = encryptMessage(myKey, myMessage)
    elif myMode == "decrypt":
        translated = decryptMessage(myKey, myMessage)

    # .title() capitalises the first letter of each word in the string
    # print either "Encrypted message:" or "Decrypted message:" based on the mode selected.
    print("%sed message:" % (myMode.title()))
    print(translated)
    print()


# Wrapper that passes the work to translateMessage() in encrypt mode.
def encryptMessage(key, message):
    return translateMessage(key, message, "encrypt")


# Wrapper, passes the work to translateMessage() in decrypt mode.
def decryptMessage(key, message):
    return translateMessage(key, message, "decrypt")


# Does the work of encrypting or decrypting the message
# The mode decides which direction the yable loppup goes
def translateMessage(key, message, mode):
    translated = []  # stores the encrypted/decrypted message string
    # Strings cannot be changed in place, so the output is built up
    # in a list, one char at a time, and then joined at the end.

    keyIndex = 0  # Stores the current position in the key
    key = key.upper()  # Makes the key uppercase, so it matches the alphabet.

    # Goes through the message, one character at a time.
    for char in message:
        # Find the characters position in the alphabet.
        # .upper() lets lowwercase match uppercase.
        # .find() returns -1 if the character is not a letter.
        num = alphabet.find(
            char.upper()
        )  # finds the index of the character in the alphabet.
        if num != -1:  # It is a letter.

            # The key letter's number picks the row in the table.
            keyNum = alphabet.find(key[keyIndex])

            if mode == "encrypt":
                # Row = key letter, Column = message letter.
                newLetter = table[keyNum][num]

            elif mode == "decrypt":
                position = table[keyNum].find(char.upper())
                newLetter = alphabet[position]

            translated.append(
                newLetter
            )  # add the encrypted/decrypted letter to the list.

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0  # wraps around to the start of the key if at the end.
        else:
            # Not a letter. Copied unchanged, always.
            translated.append(char)

    # Puts the list of characters back into one string, and returns that.
    return "".join(translated)  # returns the encrypted/decrypted message string


# Only run main() when tjis file is run directly,
# not when imported by another filee.
if __name__ == "__main__":
    main()
