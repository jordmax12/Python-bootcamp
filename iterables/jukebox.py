from albums import albums

SONGS_LIST_INDEX = 3
SONGS_TITLE_INDEX = 1
INPUT_SEP = "\n> "

while True:
    print("\nPlease choose your album\n")
    for index, metadata in enumerate(albums):
        title, artist, year, songs = metadata
        print(f"{index + 1} {title}")

    choice = int(input(INPUT_SEP))
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("\n\nPlease choose your song:\n")
    for index, (track_number, song) in enumerate(songs_list):
        print(f"{track_number}: {song}")

    song_choice = int(input(INPUT_SEP))
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_TITLE_INDEX]
        print()
        print("=" * 40)
        print(f"Playing {title}")
        print("=" * 40)