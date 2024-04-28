from random import randint
from pathlib import Path

class SubstitutionCipher:
    def __init__(self):
        self.valid_choices = ["a", "b", "c"]
        self.cipher_key = None
        self.key_vals = None

    def menu(self):
        print("""
Welcome!
-----------
a. Encrypt
b. Decrypt
c. Exit""")
        while True:
            choice = input("-> ").lower()
            if choice in self.valid_choices:
                return choice

    def _load_file(self, file_name):
        file_path = Path(file_name + ".txt")
        """ pathlib.Path.exists() returns a Boolean based on if a file exists 
        in the data directory. """
        if file_path.exists():
            with file_path.open("rt") as file:
                return [line.strip() for line in file]

    def save_file(self, file_name, contents):
        file_path = Path(file_name + ".txt")
        with file_path.open("wt") as file:
            file.write("\n".join(contents))

    def generate_key(self):
        """ chr() returns the character of a given Unicode, which generates 
        eight random ASCII characters; .join() joins all elements of an iterable 
        into one string. """
        self.cipher_key = "".join(chr(randint(33, 126)) for _ in range(8))
        self.key_vals = [ord(key_char) for key_char in self.cipher_key]
        print("Cipher Key:", self.cipher_key)
        return self.cipher_key

    def encrypt(self, plain_text, cipher_key):
        """ ord() returns the Unicode of a given character, being performed on 
        each cipher_key character. """
        key_vals = [ord(key_char) for key_char in cipher_key]
        return ["".join(self._encrypt_char(char, key_vals) for char in line) for line in plain_text]

    def _encrypt_char(self, char, key_vals):
        """ add cipher_key characters' corresponding Unicode. """
        val = ord(char) + key_vals[0]
        """ ensure the result stays within the printable ASCII range. """
        while val > 126:
            val -= 94
        while val < 33:
            val += 94
        return chr(val)

    def read_decrypted(self):
        while True:
            file_name = input("Enter file name: ")
            file_path = Path(file_name + ".txt")
            if file_path.exists():
                cipher_key = input("Enter cipher key: ")
                contents = self._load_file(file_name)
                if contents is not None:
                    return contents, cipher_key
            else:
                print("File not found.")

    def decrypt(self, cipher_text, cipher_key):
        key_vals = [ord(key_char) for key_char in cipher_key]
        return ["".join(self._decrypt_char(char, key_vals) for char in line) for line in cipher_text]

    def _decrypt_char(self, char, key_vals):
        val = ord(char) - key_vals[0]
        while val < 33:
            val += 94
        while val > 126:
            val -= 94
        return chr(val)

def main():
    """ time complexity: O(m * k), where m is the number of lines, and k is the 
    mean number of characters per line. """
    cipher = SubstitutionCipher()
    while True:
        choice = cipher.menu()
        if choice == "a":
            plain_text = input("Enter message to encrypt: ")
            cipher_key = cipher.generate_key() 
            cipher_text = cipher.encrypt([plain_text], cipher_key)
            file_name = input("Enter file name to save encrypted text as: ")
            cipher.save_file(file_name, cipher_text)
          
        elif choice == "b":
            contents, cipher_key = cipher.read_decrypted()
            cipher_text = cipher.decrypt(contents, cipher_key)
            file_name = input("Enter file name to save decrypted text as: ")
            cipher.save_file(file_name, cipher_text)
          
        elif choice == "c":
            return

if __name__ == "__main__":
    main()
