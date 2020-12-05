parrot = "Norweigan Blue"
# string indexing
print(parrot)                                                           # Norweigan Blue
print(parrot[3])                                                        # w
print(parrot[-3])                                                       # l
print(parrot[-(len(parrot))])                                           # N
print(parrot[3], parrot[4], parrot[9], parrot[3], parrot[5], parrot[8]) # w e  w i n 
# slice
print(parrot[:9])                                                       # Norweigan
print(parrot[1:])                                                       # orweigan Blue
print(parrot[1:] + parrot[1:])                                          # orweigan Blue + orweigan Blue = orweigan Blueorweigan Blue
print(parrot[:6] + parrot[6:])                                          # Norweig + an Blue = Norweigan Blue
print(parrot[:])                                                        # Norweigan Blue
print(parrot[-4:-2])                                                    # Bl
print(parrot[0:6:2])                                                    # Nre
print(parrot[0:6:3])                                                    # Nw
# slice (with double :)
number = "9,223,372,036,854,775,807"
print(number[1::4])                                                     # ,,,,,
number = "9,223;372:036 854,775;807"
print(number[1::4])                                                     # ,;: ,;
seperators = number[1::4]
print(seperators)
# slicing with step
values = "".join(char if char not in seperators else " " for char in number).split()
print(values)
print([int(val) for val in values])
# slice back
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]                                   
print(backwards)                                                        # zyxwvutsrqponmlkjihgfedcba
qpo = letters[16:13:-1]
print(qpo)                                                              # qpo
edcba = letters[4::-1]                                                  
print(edcba)                                                            # edcba
eight = letters[:-9:-1]
print(eight)                                                            # zyxwvuts

print(letters[-4:])                                                     # wxyz
print(letters[-1:])                                                     # z
letters = ""
print(letters[:1])                                                      # a works
#print(letters[0])                                                       # does not work will crash