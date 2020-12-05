# age = int(input("How old are you? "))
age = 15

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")

parrot = "Norweigan Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")