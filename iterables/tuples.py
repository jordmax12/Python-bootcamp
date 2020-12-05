t = "a", "b", "c"

# print(t)

# unpacking

a, b, c = t # must match the tuple length (a, b would fail)
# print(a, b, c)

for t in enumerate("abcdefgh"):
    pass # print(t)

metallica = ("Ride the Lightning", "Metallica", "1984")

title, artist, year = metallica
# print(title)
# print(artist)
# print(year)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# print(len(albums))

# for name, artist, year in albums:
#     print(f"Album: {name}, Artist: {artist}, Year: {year}")

# print(albums[1][3][5][1])
# print(albums[2][2])
# print(albums[3][3][3][0])
# print(albums[2][3][1])

