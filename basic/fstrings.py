greeting = "Hello"
name = "Tim"
print(greeting + " " + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age_in_words} {age} years old")

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

# Python 2 Interpolation
age = 24
major = "years"
minor = "months"
print("My age is %d %s, %d %s" %(age, major, 6, minor))
print("PI is appoximately %f" % (22 / 7))
print("PI is appoximately %12.50f" % (22 / 7))