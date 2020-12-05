# unordered, does not contain dupes
farm_animals = {
    "sheep", "cow", "hen"
}

# print(farm_animals)

for animal in farm_animals:
    pass # print(animal)

SEP = "*" * 40
print(SEP)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# can pass in any iterable object (set or range as well)

# print(wild_animals)

empty_set = set()
empty_set.add("a")

even = set(range(0, 40, 2))
print(f"EVEN {even}")
print(f"EVEN LEN {len(even)}")
square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(f"SQUARES LEN {len(squares)}")

# union = combines 2 sets

print(f"EVEN UNION SQUARES: {even.union(squares)}")
print(f"LEN EVEN UNION SQUARES: {len(even.union(squares))}")

print(SEP)

# intersection = sets of matching values

print(f"EVEN INTERSECTION SQUARES {even.intersection(squares)}")
print(f"EVEN INTERSECTION SQUARES 2 {even & squares}") # same way to do intersection
print(f"SQUARES INTERSECTION EVEN {squares.intersection(even)}")
print(f"SQUARES INTERSECTION EVEN 2 {squares & even}")

print(SEP)

# difference = remove matching sets

print(f"EVEN DIFFERENCE SQUARES: {sorted(even.difference(squares))}")
print(f"EVEN DIFFERENCE SQUARES 2: {sorted(even - squares)}")
print(f"SQUARES DIFFERENCE EVEN: {sorted(squares.difference(even))}")
print(f"SQUARES DIFFERENCE EVEN 2: {sorted(squares - even)}")

print(SEP)

# difference_update = updates the original set
# print("DIFFERENCE UPDATE")
# print(f"BEFORE: {sorted(even)}")
# even.difference_update(squares)
# print(f"AFTER {sorted(even)}")

print(SEP)

# symmetric difference - all the members that are in set A, but not both
# could be thought of as the opposite of intersection
print("SYMMETRIC DIFFERENCE")
print(f"EVEN BEFORE: {sorted(even)}")
print(f"EVEN AFTER {sorted(even.symmetric_difference(squares))}")
print(f"SQUARES BEFORE: {sorted(squares)}")
print(f"SQUARES AFTER {sorted(squares.symmetric_difference(even))}")
# alternate way of using carrots

print(SEP)

# Removing items from set
# discard will not raise error if not exist
# remove will raise error if not exist
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)

# print(squares)
# squares.remove(8) # throws error
if 8 in squares: # proper way
    squares.remove(8)

# OR

# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")

# is_sub_set = one set is a sub_set of another if all the members are contained
# in the other set
# is_super_set = one set is a super_set of another if it contains all the other
# sets members

squares_tuple = (4,6,16)
squares = set(squares_tuple)
even = set(range(0, 40, 2))

print(squares, even)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a super set of squares")

# frozensets = immutable, otherwise the same as other sets
even = frozenset(range(0,100,2))

print(even)

