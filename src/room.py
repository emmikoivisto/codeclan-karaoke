class Room:
    def __init__(self, name, guest_list):
        self.name = name
        self.guest_list = guest_list
        self.playlist = []

    
    def add_songs_to_playlist(self, new_song):
        self.playlist.append(new_song)

    def guest_count(self):
        return len(self.guest_list)

    def add_guest_to_guestlist(self, new_guest):
        return self.guest_list.append(new_guest)

    def remove_guest_from_guestlist(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)