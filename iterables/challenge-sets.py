sample_text = "Python is a very powerful language"

vowels = frozenset("aeiou")
final_set = set(sample_text).difference(vowels)

print(final_set)
final_list = sorted(final_set)
print(final_list)