fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow, cirtus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": 'sour, green citrus fruit'
}

# print(fruit)
# print(fruit["lemon"])

# dictionaries are mutable
fruit["pear"] = "an odd shaped apple"

# dictionaries guarantee the unique key
fruit["pear"] = "great with tequila"

# print(fruit["pear"]) # great with tequila

# del fruit["lemon"] # delete item by key

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key.casefold() == "quit":
#         break
#     description = fruit.get(dict_key.casefold(), f"We don't have a {dict_key}")
#     # get on dictionary supports default value.
#     # if dict_key in fruit
#     print(f"\n{description}\n")

# order a dictionary if needed ordered and guaranteed
# ordered_keys = list(fruit.keys()) 
# ordered_keys.sort()
# fruit.values() also works, but is less optimized than getting keys
ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    pass # print(f"{f} - {fruit[f]}")


# print(fruit.items())
f_tuple = tuple(fruit.items()) # convert dictionary to tuple
# print(dict(f_tuple))
f_list = list(fruit.items()) # not sure if this is working properly lol
# print(f_list)

# joins
my_list = ["a", "b", "c"]
new_string = ", ".join(my_list)

# print(new_string)
locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of the hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest",
}

exits = [
    {
        "Q": 0
    },
    {
        "N": 5,
        "E": 3,
        "S": 4,
        "W": 2,
        "Q": 0
    },
    {
        "N": 5,
        "Q": 0
    },
    {
        "W": 1,
        "Q": 0
    },
    {
        "N": 1,
        "W": 2,
        "Q": 0
    },
    {
        "S": 1,
        "W": 2,
        "Q": 0
    }
]

loc = 1
while True:
    available_exists = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     available_exists += f"{direction}, "
    
    print(locations[loc])

    if loc == 0:
        break

    direction = input(f"Available exists are {available_exists}").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")

