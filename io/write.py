cities = ["LA", "Chicago", "NYC", "San Francisco", "Ontario"]

# write line by line, not very practical
# with open("../data/cities.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)

imelda = "More Mayhem", "Imedla May", "2011", (
    (1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

# with open("../data/imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)

# this code is pretty pointless? not sure what he was getting at
# with open("../data/imelda3.txt", "r") as imelda_file:
#     contents = imelda_file.readline()

# imedla = eval(contents)

# print(imelda)
# title, artist, year, songs = imelda
# print(title, artist, year, songs)

# appending
with open("../data/imelda3.txt", "a") as imelda_file:
    print(imelda, file=imelda_file)