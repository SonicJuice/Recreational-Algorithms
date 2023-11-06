from random import randint
from os import path

def displayMenu():
    print('''Welcome!

a. Encrypt
b. Decrypt
c. Exit
''')

#---------------------------------------------------------

def menuChoice():
    valid_choices = ["a", "b", "c"]
    while True:
        choice = input("-> ").lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice; please try again.")

#---------------------------------------------------------

def loadFile(file_name):
    try:
        with open(file_name, "rt") as file:
            """ '.strip()' removes leading & trailing whitespace, which is performed for each line. """
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File '{file_name}' not found; please try again.")
        return None

#---------------------------------------------------------

def saveFile(file_name, contents):
    with open(file_name, "wt") as file:
        """ write the contents to the file with newline separators. """
        file.write("\n".join(contents))

#---------------------------------------------------------

def generateKey():
    """ 'chr()' returns the character of a given Unicode code, which generates eight random ASCII characters; '.join()' returns a 
    string by joining all elements of an iterable. '_' is a placeholder for generated values. """
    cypher_key = "".join(chr(randint(33, 126)) for _ in range(8))
    print("Cypher Key:", cypher_key)
    return cypher_key

#---------------------------------------------------------

def encrypt(plain_text, cypher_key):
    """ 'ord()' returns the Unicode code of a given character, being performed on each 'cypher_key' character. """
    key_vals = [ord(key_char) for key_char in cypher_key]
    """ 'zip()' aggregates iterables into a tuple, encrypting each 'plain_text' character via 'cypher_key'. """
    return [
        "".join(encryptChar(char, key_char, key_vals) for char, key_char in zip(line, cypher_key))
        for line in plain_text
    ]

#---------------------------------------------------------

def encryptChar(char, key_char, key_vals):
    val = ord(char)
    """ add 'cypher_key' characters' corresponding Unicode codes. """
    val += key_vals[0]
    """ ensures the result stays within the printable ASCII range. """
    while val > 126:
        val -= 94
    while val < 33:
        val += 94
    """ 'chr()' returns the character of a given Unicode code. """
    return chr(val)

#---------------------------------------------------------

def readDecrypted():
    while True:
        file_name = input("Enter file name: ")
        """ 'os.path.exists()' checks the existance of a given directory. """
        if path.exists(file_name):
            cypher_key = input("Enter cypher key: ")
            contents = loadFile(file_name)
            if contents is not None:
                return contents, cypher_key
        else:
            print(f"File '{file_name}' not found; please try again.")

#---------------------------------------------------------

def decrypt(cypher_text, cypher_key):
    key_vals = [ord(key_char) for key_char in cypher_key]
    return [
        "".join(decryptChar(char, key_char, key_vals) for char, key_char in zip(line, cypher_key))
        for line in cypher_text
    ]

#---------------------------------------------------------

def decryptChar(char, key_char, key_vals):
    val = ord(char)
    val -= key_vals[0]
    while val < 33:
        val += 94
    while val > 126:
        val -= 94
    return chr(val)

#---------------------------------------------------------

def main():
    while True:
        displayMenu()
        choice = menuChoice()

        if choice == 'a':
            plain_text = input("Enter message to encrypt: ")
            cypher_key = generateKey()
            cypher_text = encrypt(plain_text, cypher_key)
            file_name = input("Enter file name to save encrypted text: ")
            saveFile(file_name, cypher_text)

        elif choice == 'b':
            contents, cypher_key = readDecrypted()
            plain_text = decrypt(contents, cypher_key)
            file_name = input("Enter file name to save decrypted text: ")
            saveFile(file_name, plain_text)

        elif choice == 'c':
            return

#---------------------------------------------------------

if __name__ == '__main__':
    main()

""" time complexity: 'O(m * k)', where 'm' is the number of lines, and 'k' is the average number of characters per line' """
