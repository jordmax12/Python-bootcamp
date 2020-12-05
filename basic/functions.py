def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz
 
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
 
 
for i in range(1, 101):
    pass # print(fizz_buzz(i))

def is_palindrome(string):
    return string.casefold() == string[::-1].casefold()

def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()

word = input("Please enter word to check")

if is_palindrome_sentence(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")