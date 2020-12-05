choices = [
    "Exit",
    "Learn Python",
    "Learn Java",
    "Go Swimming",
    "Have dinner",
    "Go to bed"
]

menu = """
Please choose you option from the list below:\n
"""

i = 1
while i < len(choices):
    menu += f"{str(i)}. {choices[i]}\n"
    i += 1

menu += "0. Exit\n\n> "

def show_menu():
    selection = input(menu)
    count = len(choices) - 1
    try:
        int_selection = int(selection)
        mapped = choices[int_selection]
        print()
        if (1 <= int_selection <= count):
            print("*" * 80)
            print(f"\n\nYou selected {mapped}\n\n")
            print("*" * 80)
            return True
        else:
            return False

    except:
        print("*" * 80)
        print(f"\n\nUnknown selection: {selection}\tPlease try again\n\n")
        print("*" * 80)
        return True

should_show_again = True

while should_show_again:
    should_show_again = show_menu()