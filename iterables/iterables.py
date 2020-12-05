shopping_list = [
    "milk",
    "pasta",
    "eggs",
    "spam",
    "bread",
    "rice"
]

# print(id(shopping_list))
shopping_list += ["cookies"]
# print(id(shopping_list))
shopping_list.append("cream")
# print(shopping_list)
a = b = shopping_list # bind a and b to shopping_list
# print(a)
shopping_list.pop()
# print(shopping_list, a) # a will be changed

even = [2,4,6,8]
odd = [1,3,5,7,9]

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# print(len(even))
# print(len(even))
# print("mississippi".count("s"))

computer_parts = [
    "gpu",
    "memory",
    "storage",
    "cpu",
    "fans",
    "case"
]

for index, part in enumerate(computer_parts):
    print(f"{index}: {part}")

for index, character in enumerate("test string"):
    print(f"{index}: {character}")

valid_choices = [str(i) for i in range(1, len(computer_parts) + 1)]

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd) # combine 2 lists

even.sort() # sorts? what if objects though?
even.sort(reverse=True)
