# filepath: /c:/Users/khuu1/bmttnangcao/Lab02/cipher/caesar/caesar_cipher.py
from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, shift: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + shift) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            else:
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, shift: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - shift) % alphabet_len
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter)
            else:
                decrypted_text.append(letter)
        return "".join(decrypted_text)