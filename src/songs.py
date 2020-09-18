class Songs:
    
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.playlist = []

    
    def add_songs_to_playlist(self, new_song):
        self.playlist.append(new_song)