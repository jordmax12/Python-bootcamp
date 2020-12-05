available_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "hdmi cable",
    "dvd drive"
]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"You current cart contains {computer_parts}")
    else:
        print("Please add options from the list below")
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")
    
    current_choice = input()

print(computer_parts)