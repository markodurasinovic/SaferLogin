import random
import string

def generate_username(length=8):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))

def generate_password(length=16):
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for i in range(length))
