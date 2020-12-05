import random

max = 100

answer = random.randint(1, max)

print(answer)

print(f"Please guess the number between 1 and {max}: ")
guess = int(input())

while True:
    if guess == 0:
        break

    if guess != answer:
        print("Please guess again")
        guess = int(input())
    else:
        break

print("Complete!")