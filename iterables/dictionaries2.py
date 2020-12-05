fruits = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow, cirtus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": 'sour, green citrus fruit'
}

vegetables = {
    "cabbage": "every child's favorite",
    "sprouts": "mmmm, lovely",
    "spinach": "can I have some more fruit, please?"
}

# combine 2 dictionaries
vegetables.update(fruits)

print(vegetables)

# or we can use copy instead to not change the original dictionary
nice_and_nasty = fruits.copy()
nice_and_nasty.update(vegetables)
print(nice_and_nasty)