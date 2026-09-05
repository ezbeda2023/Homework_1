"""Interactive Caesar cipher and letter-frequency analyzer."""


def caesar_cipher(text, shift):
    """Return text with each letter shifted by shift positions."""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    shift = shift % 26

    for character in text:
        if character in lowercase:
            index = lowercase.index(character)
            encrypted += lowercase[(index + shift) % 26]
        elif character in uppercase:
            index = uppercase.index(character)
            encrypted += uppercase[(index + shift) % 26]
        else:
            encrypted += character

    return encrypted


def caesar_decipher(cyphertext, shift):
    """Decrypt text that was encrypted with the given Caesar shift."""
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    """Return case-insensitive counts for every letter in the alphabet."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequencies = {}

    for letter in alphabet:
        frequencies[letter] = 0

    for character in text:
        lowercase_character = character.lower()
        if lowercase_character in alphabet:
            frequencies[lowercase_character] += 1

    return frequencies


def main():
    """Run the interactive Caesar-cipher menu."""
    while True:
        print("\nCaesar Cipher Menu")
        print("1. Encrypt, analyze, and decrypt a message")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter a message: ")
            shift = int(input("Enter a shift value: "))

            ciphered_text = caesar_cipher(message, shift)
            frequencies = letter_frequency(message)
            deciphered_text = caesar_decipher(ciphered_text, shift)

            print("\nCiphered text:", ciphered_text)
            print("\nLetter frequencies:")
            for letter in frequencies:
                print("{}: {}".format(letter, frequencies[letter]))
            print("\nDeciphered text:", deciphered_text)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
