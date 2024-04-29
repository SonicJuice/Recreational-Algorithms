import string
import logging
from datetime import datetime


class SubstitutionCipher:
    def __init__(self):
        self.jumps = 0
        self.alphabet = string.ascii_lowercase
        self.shifted_alphabet = {}
        """ logging.getLogger returns a reference to a logger instance with the 
        specified name to record events during program execution. """
        self.logger = logging.getLogger("SubstitutionCipher")

    def instantiate(self):
        while True:
            try:
                self.jumps = int(input("Enter the preferred number of character jumps (1-26): "))
                if 1 <= self.jumps <= 26:
                    self._initialize_shifted_alphabets()
                    """ logging.info() records events within the parameters of 
                    expected behavior. """
                    self.logger.info(f"Encryption parameters set with jumps: {self.jumps}")
                    return self.jumps
            except ValueError:
                """ logging.error() records unexpected failures. """
                self.logger.error("Invalid input for jumps, must be an integer.")

    def _initialize_shifted_alphabets(self):
        """ initialise shifted encryption/decryption alphabets. """
        self.shifted_alphabet["encrypt"] = self.alphabet[self.jumps:] + self.alphabet[:self.jumps]
        self.shifted_alphabet["decrypt"] = self.alphabet[-self.jumps:] + self.alphabet[:-self.jumps]

    def _transform_text(self, text, mode):
        """ str.maketrans() creates a one to one mapping of a character to its 
        translation. str.translate() returns a string where each character is 
        mapped to its corresponding character in the translation table. 
        .upper() returns a string of all upper case characters. """
        transform_map = str.maketrans(
            self.alphabet + self.alphabet.upper(),
            self.shifted_alphabet[mode] + self.shifted_alphabet[mode].upper()
        )
        transformed_text = text.translate(transform_map)
        return transformed_text

    def encrypt(self):
        if self.jumps == 0:
            print("Number of character jumps not set.")
            return self.logger.error("Number of character jumps not set.")
        plain_text = input("Enter text: ")
        cipher_text = self._transform_text(plain_text, "encrypt")
        print(cipher_text)
        self.logger.info(f"Encrypted '{plain_text}' to '{cipher_text}'")

    def decrypt(self):
        if self.jumps == 0:
            print("Number of character jumps not set.")
            return self.logger.error("Number of character jumps not set.")
        cipher_text = input("Enter text: ")
        plain_text = self._transform_text(cipher_text, "decrypt")
        print(plain_text)
        self.logger.info(f"Decrypted '{cipher_text}' to '{plain_text}'")

    def menu(self):
        exit_flag = False
        while not exit_flag:
            print("""
1. Instantiate encryption parameters
2. Encrypt text
3. Decrypt text
4. Reset encryption parameters
5. Exit
""")
            choice = input("-> ")

            if choice == "1":
                self.instantiate()
                input("Press Enter to continue...")

            elif choice == "2":
                self.encrypt()
                input("Press Enter to continue...")

            elif choice == "3":
                self.decrypt()
                input("Press Enter to continue...")

            elif choice == "4":
                self.jumps = 0
                self.shifted_alphabet.clear()
                self.logger.info("Encryption parameters reset.")
                print("Resetting...")
                input("Press Enter to continue...")

            elif choice == "5":
                print("Exiting...")
                exit_flag = True

if __name__ == "__main__":
    """ logging.basicConfig() establishes the default behaviour of the 
    logging system in terms of message severity and format. """
    logging.basicConfig(filename="substiution_cipher.log", level=logging.INFO,
      format="%(asctime)s - %(levelname)s - %(message)s")
    """ time complexity: O(n). """
    SubstitutionCipher().menu()
