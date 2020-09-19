class Room:
    def __init__(self, name, guest_list):
        self.name = name
        self.guest_list = guest_list
        self.playlist = []

    
    def add_songs_to_playlist(self, new_song):
        self.playlist.append(new_song)

    def guest_count(self):
        return len(self.guest_list)