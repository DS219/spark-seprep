import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range(12))

print("Your generated password is:", password)