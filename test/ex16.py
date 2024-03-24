class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_birthday = Song(["Happy birthday to you",
                        "I don't want to get sued",
                        "So I stop right there"])
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

txt = open("ex16_sample.txt")
txt_content = txt.read()
txt.seek(0)
print(txt.read())
my_txt = Song(txt_content.splitlines())
my_txt.sing_me_a_song()
