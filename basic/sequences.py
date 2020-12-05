computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
print(computer_parts[1][0][0][0][0])                    # m
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5) # he's probably pining for the fjords
print("Hello " * 5)                                    # Hello Hello Hello Hello Hello

today = "friday"
print("day" in today)                                   # True
print("fri" in today)                                   # True
print("thur" in today)                                  # False
print("parrot" in "fjord")                              # False

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[:-1:5])
print(data[1:5])
print(data[0:-1:5])

age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
print("""There 
are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and 
{7}
""".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3)) # why ever do this just dont use precision at all ex: and cubed is {2} why give it precision?

# automatic field numbering (cannot switch from this and use manual field specification example, cant do this: No. {} squared is {1} this mixes automatic and manual, python will error out
for i in range(1,13):
    print("No. {:<2} squared is {:<3} and cubed is {:<4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22/7))         # 3.142857142857143 (width = 12, but override since its larger, if we did 0:18, we would see the width grow (the default formatting returns 17 digits for this calc))
print("Pi is approximately {0:12f}".format(22/7))        #     3.142857 (12 total widths, 3. = 2, 6 after decimal, and 4 empty = 12)
print("Pi is approximately {0:12.50f}".format(22/7))    # 3.14285714285714279370154144999105483293533325195312 (12 width gets overridden by the 50f, which means, i want 50 places after the decimal, which is more than 12, so its overridden)
print("Pi is approximately {0:52.50f}".format(22/7))    # 3.14285714285714279370154144999105483293533325195312 (same amount, so its the same as above (52 total, with 50 after decimal + 3. = 52))
print("Pi is approximately {0:62.50f}".format(22/7))    #           3.14285714285714279370154144999105483293533325195312 (same as above but now the width gets applied since there is room)
print("Pi is approximately {0:72.50f}".format(22/7))    #                     3.14285714285714279370154144999105483293533325195312 (same as above but now the width gets applied since there is room)
print("Pi is approximately {0:<72.50f}".format(22/7))    #                     3.14285714285714279370154144999105483293533325195312 (same as above but now the width is a less than, so it wont do extra room if not needed)
print("Pi is approximately {0:82.60f}".format(22/7))    #                     3.142857142857142793701541449991054832935333251953125000000000 (example showing if you want more than 50, although this seems to be python limit)


