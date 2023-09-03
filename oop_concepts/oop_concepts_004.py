## create a class called Song
## i want that class to sing a song or print lyrics line by line
import time

class Song:
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            time.sleep(1)

bappy_bday_song = [
    "Happy birthday to you",
    "I dont want to get sued",
    "So i am stopping here"
]

bulls_on_parade = [
    "They rally around the family",
    "With pockets full of shells",
]

my_first_song = Song(bappy_bday_song)
my_first_song.sing_me_a_song()

print("Your first song is done \n\n")

my_second_song = Song(bulls_on_parade)
my_second_song.sing_me_a_song()