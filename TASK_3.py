import random
import string

print("\n=======> PASSWORD GENERATOR <=======\n")
password = str()
while True:
    try:
        length = int(input("Enter the length of the password: "))
        break
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

generate = string.ascii_letters + string.digits + string.punctuation
for _ in range(length):
    password += random.choice(generate)
print(f"Generated Password: {password}")



