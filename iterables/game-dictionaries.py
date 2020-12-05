locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of the hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest",
}

exits = {
    0: {"Q": 0 },
    1: {"N": 5, "E": 3, "S": 4, "W": 2, "Q": 0},
    2: {"N": 5, "Q": 0 },
    3: {"W": 1, "Q": 0 },
    4: {"N": 1, "W": 2, "Q": 0 },
    5: {"S": 1, "W": 2, "Q": 0 },
}

named_exits = {
    1: {"2": 2, "3": 3, "4": 4},
    2: {"5": 5},
    3: {"1": 1},
    4: {"1": 1, "2": 2},
    5: {"1": 1, "2": 2},
}

vocabulary = {
    "QUIT":  "Q",
    "NORTH": "N",
    "EAST":  "E",
    "SOUTH": "S",
    "WEST":  "W",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5",
}

loc = 1
while True:
    available_exists = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     available_exists += f"{direction}, "
    SEP = "*" * 80
    print(f"\n{SEP}")
    print(f"\n{locations[loc]}\n")
    print(f"{SEP}\n")

    if loc == 0:
        break
    else:
        all_exits = exits[loc].copy()
        all_exits.update(named_exits[loc])

    direction = input(f"Available exists are {available_exists}\n\n> ").upper()
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

    print(f"direction {direction}", all_exits, loc)
    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print(f"\n{SEP}")
        print("\n\nERROR: You cannot go in that direction\n\n")
        print(f"{SEP}\n")