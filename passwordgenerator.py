import random

length = 6

password = ""

for _ in range(length):
    password += str(random.randint(1,9))

print(password)