import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated password:", generate_password(length=16))
