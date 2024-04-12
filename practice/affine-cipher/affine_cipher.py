"""
Approach:
- The provided code implements a simple affine cipher, which is a type of substitution cipher.
- The `encode` function encodes plain text using the formula E(x) = (ax + b) mod m, where 'a' and 'm' are coprime, and 'b' is any integer.
- The `decode` function decodes the ciphered text using the formula D(x) = a^(-1)(x - b) mod m.
- The `is_coprime` function checks whether two numbers are coprime.
- The implementation ensures that 'a' and the length of the alphabet are coprime to ensure that every letter is mapped to a unique value.
"""

import math
import string

def is_coprime(x, y):
    return math.gcd(x, y) == 1

def encode(plain_text, a, b):
    alphabet = list(string.ascii_lowercase)
    numbers = list(string.digits)
    if not is_coprime(a, len(alphabet)):
        raise ValueError("a and m must be coprime.")
    indexes = []
    for letter in plain_text.lower():
        if letter in alphabet:
            indexes.append((a * alphabet.index(letter) + b) % len(alphabet))
        elif letter in numbers:
            indexes.append(int(letter) + 1000)
    out = ""
    for place, index in enumerate(indexes):
        if place % 5 == 0 and place > 1:
            out += " "
            if index < len(alphabet):
                out += alphabet[index]
            else:
                out += str(index - 1000)
        else:
            if index < len(alphabet):
                out += alphabet[index]
            else:
                out += str(index - 1000)
    return out

def decode(ciphered_text, a, b):
    alphabet = list(string.ascii_lowercase)
    numbers = list(string.digits)
    if not is_coprime(a, len(alphabet)):
        raise ValueError("a and m must be coprime.")
    indexes = []
    for letter in ciphered_text:
        if letter in numbers:
            indexes.append(int(letter) + 1000)
        elif letter in alphabet:
            indexes.append(
                pow(a, -1, len(alphabet)) * (alphabet.index(letter) - b) % len(alphabet)
            )
    return "".join(
        [
            str(letter - 1000) if letter > len(alphabet) else alphabet[letter]
            for letter in indexes
        ]
    )
