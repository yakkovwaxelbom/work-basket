import random


class Track:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

        self.stop()

    @property
    def name(self):
        return self._name
    @property
    def artist(self):
        return self._artist

    @property
    def duration(self):
        return self._duration

    @name.setter
    def name(self, name):
        self._name = str(name)

    @artist.setter
    def artist(self, artist):
        self._artist = str(artist)

    @duration.setter
    def duration(self, duration):
        if duration > 0:
            self._duration = duration
        else:
            raise ValueError('Invalid track duration')

    def stop(self):
        self.is_player = False

    def play(self):
        self.is_player = True

    def __repr__(self):
        return f'({self.name}:{self.duration})'


track1 = Track('yakov', 'yakov', 220)


# print(track1)


class Commercial(Track):
    def __init__(self, artist):
        super().__init__(name='commercial', artist=artist, duration=60)

    def play(self):
        print(f'For more songs By {self.artist},go to GoodVibes website')
        super().play()


c = Commercial('ABBA')
# c.stop()
c.play()
print(c)
print(c.is_player)


class Player:
    def __init__(self, tracks: list):  # לברר יותר איך זה עובד כלומר האם אפשר להוסיף באופן ידני רצועות
        self.tracks = tracks

    @property
    def tracks(self):
        return self._tracks

    @tracks.setter
    def tracks(self, tracks):
        set_of_artists = {song.artist for song in tracks}
        for artist in set_of_artists:
            self._tracks.append(Commercial(artist))
        self.current = -1

    def next(self, rand=False):
        if not rand:
            if self.current < len(self.tracks) - 2 and self.tracks[self.current].is_player:
                self.tracks[self.current].is_player = False
                self.current += 1
                self.tracks[self.current].is_player = True
            else:
                if self.current == len(self.tracks) and self.tracks[self.current].is_player:
                    self.tracks[self.current].is_player = False
                    self.current = 0
                    self.tracks[self.current].is_player = True
                else:
                    self.current = 0
                    self.tracks[self.current].is_player = True
        else:
            current = random.randint(0, len(self.tracks))
            self.current = current
            self.tracks[self.current].is_player = True
