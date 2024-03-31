from random import randint
from pathlib import Path


class SubstitutionCipher:
    def __init__(self):
        self.valid_choices = ["a", "b", "c"]
        self.cypher_key = None

    def menu(self):
        print(""" Welcome!
        a. Encrypt
        b. Decrypt
        c. Exit
        """)
        while True:
            choice = input("-> ").lower()
            if choice in self.valid_choices:
                return choice

    def _load_file(self, file_name):
        try:
            with open(file_name, "rt") as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            print(f"{file_name} not found.")
            return

    def save_file(self, file_name, contents):
        with open(file_name, "wt") as file:
            file.write("\n".join(contents))

    def generate_key(self):
        """ 'chr()' returns the character of a given Unicode, which generates eight random ASCII characters; 
        '.join()' returns a string """
        self.cypher_key = "".join(chr(randint(33, 126)) for _ in range(8))
        print("Cypher Key:", self.cypher_key)

    def encrypt(self, plain_text):
        if self.cypher_key is None:
            print("Cypher key not generated.")
            return
        """ 'ord()' returns the Unicode of a given character, being performed on each 'cypher_key' character. """
        key_vals = [ord(key_char) for key_char in self.cypher_key]
        return ["".join(self._encrypt_char(char, key_char, key_vals) for char, key_char in zip(line, self.cypher_key))
            for line in plain_text]

    def _encrypt_char(self, char, key_char, key_vals):
        val = ord(char)
        """ add 'cypher_key' characters' corresponding Unicode. """
        val += key_vals[0]
        """ ensure the result stays within the printable ASCII range. """
        while val > 126:
            val -= 94
        while val < 33:
            val += 94
        return chr(val)

    def read_decrypted(self):
        while True:
            file_name = input("Enter file name: ")
            if Path.exists(file_name):
                cypher_key = input("Enter cypher key: ")
                contents = self._load_file(file_name)
                if contents is not None:
                    return contents, cypher_key
            else:
                print(f"File '{file_name}' not found.")

    def decrypt(self, cypher_text):
        if self.cypher_key is None:
            print("Cypher key not provided.")
            return
        key_vals = [ord(key_char) for key_char in self.cypher_key]
        return ["".join(self._decrypt_char(char, key_char, key_vals) for char, key_char in zip(line, self.cypher_key))
            for line in cypher_text]

    def _decrypt_char(self, char, key_char, key_vals):
        val = ord(char)
        val -= key_vals[0]
        while val < 33:
            val += 94
        while val > 126:
            val -= 94
        return chr(val)

def main(self):
    cipher = SubstitutionCipher()
    while True:
        choice = cipher.menu()
        if choice == "a":
            plain_text = input("Enter message to encrypt: ")
            cipher.generate_key()
            cypher_text = cipher.encrypt(plain_text)
            file_name = input("Enter file name to save encrypted text as: ")
            cipher.save_file(file_name, cypher_text)
        elif choice == "b":
            contents, cypher_key = cipher.read_decrypted()
            cipher.cypher_key = cypher_key
            plain_text = self.decrypt(contents)
            file_name = input("Enter file name to save decrypted text as: ")
            cipher.save_file(file_name, plain_text)
        elif choice == "c":
            return
            
if __name__ == '__main__':
    """ time complexity: 'O(m * k)', where 'm' is the number of lines, and 'k' is the average number of characters per line """
    main()
