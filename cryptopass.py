import random
import string

def generate_password(length):
    # Define the set of characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Example usage
password_length = 12
password = generate_password(password_length)
print(password)
