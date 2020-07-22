class Song(object):

    def __init__(self, lyrics, artist):
        self.lyrics = lyrics
        self.artist = artist

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    def who_sung_that(self):
        print(self.artist)

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"], "Zed")

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"], "Fred, probably")

happy_bday.sing_me_a_song()
happy_bday.who_sung_that()


bulls_on_parade.sing_me_a_song()
bulls_on_parade.who_sung_that()


problem = ["Hey, baby even though I hate ya",
            "I wanna love ya",
            "I want you",
            "And even though I can't forgive ya",
            "I really want to",
            "I want you"]

ariana = Song(problem, "Ariana Grande")

ariana.sing_me_a_song()
ariana.who_sung_that()
