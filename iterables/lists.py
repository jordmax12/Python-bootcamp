computer_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mousepad"
]

# ok this is obvious lets get to advanced stuff omegalool
# for part in computer_parts:
#     print(part)

# print()
# print(computer_parts[2])

# print(computer_parts[0:3])
# print(computer_parts[-1])

digits = list("432985617")
more_digits_copy = list(digits)
more_digits_copy_two = digits.copy()

computer_parts[3:] = ["trackball"] # replaces the slice range with the 
                                   # iteratable you provide
del computer_parts[0:2] # deletes items within this slice range

data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 
        185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# process low values in the list
stop = 0

for index, value in enumerate(data):
    if (value >= min_valid):
        stop = index
        break

print(stop)
del data[:stop] # although this is pretty useless bc we dont remove the max
                # and we'd have to iterate over the array again

# reversed function
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        print(top_index - index, value)
        del data[top_index - index]

print(data)

empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even, odd]
print(numbers)

# unpacking lists

data_list = [12,13,14]
p, q, r = data_list # unpacking must match the list length
print(p, q, r)