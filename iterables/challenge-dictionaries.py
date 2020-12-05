locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of the hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest",
}

# exits = [
#     {
#         "Q": 0
#     },
#     {
#         "N": 5,
#         "E": 3,
#         "S": 4,
#         "W": 2,
#         "Q": 0
#     },
#     {
#         "N": 5,
#         "Q": 0
#     },
#     {
#         "W": 1,
#         "Q": 0
#     },
#     {
#         "N": 1,
#         "W": 2,
#         "Q": 0
#     },
#     {
#         "S": 1,
#         "W": 2,
#         "Q": 0
#     }
# ]

exits = {
    0: {"Q": 0 },
    1: {"N": 5, "E": 3, "S": 4, "W": 2, "Q": 0},
    2: {"N": 5, "Q": 0 },
    3: {"W": 1, "Q": 0 },
    4: {"N": 1, "W": 2, "Q": 0 },
    5: {"S": 1, "W": 2, "Q": 0 },
}

vocabulary = {
    "QUIT":  "Q",
    "NORTH": "N",
    "EAST":  "E",
    "SOUTH": "S",
    "WEST":  "W",
}

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
    # Parse user input, using our vocabular dict if necessary
    if len(direction) > 1:
        # for word in vocabulary: # does it contain a word we know
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")