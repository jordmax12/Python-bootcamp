class Song:
    """Class to represent a song

    Attributes:
        name (str): The name of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, name, artist, duration=0):
        self.name = name
        self.artist = artist
        self.duration = duration

    def get_name(self):
        return self.name

    name = property(get_name)