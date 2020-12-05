for i in range(1,21):
    print("i is now {}".format(i))

print("*" * 80)

for i in range(1,21,2):
    print("i is now {}".format(i))

print("*" * 80)

for i in range(21,1,-5):
    print("i is now {}".format(i))

print("*" * 80)

age = int(input("How old are you? "))

if age in range(16,65):
    print("Have good day at work")
else:
    print("Go to school")