import random

print("Password Generator")
length = int(input("Enter the desired password length: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
number = int(input("Amount of passwords to generate: "))
for _ in range(number):
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

print("Password generation complete.")