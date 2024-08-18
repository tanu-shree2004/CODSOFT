import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
password = generate_password(length)
print(f"Generated password: {password}")