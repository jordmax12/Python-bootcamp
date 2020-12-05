import random

low = 1
high = 1000
print(r"C:\Users\timbuchalka\notes.txt")
print(f"Enter a number between {low} and {high}: ")

guesses = 1
while True:
    print(f"\tGuessing in the range of {low} and {high}")
    guess =  low + (high - low) // 2
    high_low = input(f"""My guess is: {guess}. Should I guess higher or lower? 
    Enter h or l, or c if my guess was correct\n""").casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("Please enter h, l or c")

    guesses += 1