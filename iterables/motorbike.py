bike = {
    "make": "Honda",
    "model": "250 dream",
    "color": "red",
    "engine_size": 250,
    "tupple": (1,2,3),
    "list": ["123"]
}

print(bike["color"])
print(bike["tupple"])

# dictionaries are mutable
bike["chrome"] = True
print(bike["chrome"])