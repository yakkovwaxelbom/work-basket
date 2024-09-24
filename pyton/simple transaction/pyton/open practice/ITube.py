import random


class Clip:
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year
        self.stop()

    @property
    def name(self):
        return self._name

    @property
    def year(self):
        return self._year

    def __str__(self):
        return f'{self.name}:{self.year}'

    def __repr__(self):
        return self.__str__()

    def stop(self):
        self.is_player = False

    def play(self):
        self.is_player = True

    @name.setter
    def name(self, name):
        self._name = str(name)

    @year.setter
    def year(self, year):
        if year == int(year):
            self._year = year
        else:
            raise ValueError('')


class ArtClip(Clip):
    def __init__(self, name: str, year: int, time: int):
        super().__init__(name, year)
        self.time = time

    def is_valid_for_euro(self):
        return self.time <= 3

    @property
    def time(self):
        return self._time

    def __str__(self):
        return f'{self.name}:{self.year}  ({self.time})'

    def __repr__(self):
        return self.__str__()

    @time.setter
    def time(self, time):
        self._time = int(time)


class Player:
    def __init__(self, clips: list):  # לברר יותר איך זה עובד כלומר האם אפשר להוסיף באופן ידני רצועות
        self.clips = clips

    @property
    def clips(self):
        return self._clips

    @clips.setter
    def clips(self, clips):
        for clip in clips:
            if type(clip) != Clip or type(clip) != ArtClip:
                raise ValueError('')  # לברר יותר אם יש בעיה אז האובייקט נופל או שלא
        self._clips = clips
        self.current = -1

    def next(self):  # כנראה שאפשר לבנות בו משהו בסגנון FIFO
        if self.current < len(self.clips) - 2 and self.clips[self.current].is_player:
            self.clips[self.current].is_player = False
            self.current += 1
            self.clips[self.current].is_player = True
        elif self.current == len(self.clips) and self.clips[self.current].is_player:
            self.clips[self.current].is_player = False
            self.current = 0
            self.clips[self.current].is_player = True
        elif self.current == len(self.clips) or self.current == -1:
            self.current = 0
            self.clips[self.current].is_player = True
        else:
            raise ValueError('')

    def shuffle(self):
        for i in range(len(self.clips)):
            j = random.randint(0, len(self.clips) - 1)  # j = random.randint(i, len(self.clips) - 1)
            self.clips[i], self.clips[j] = self.clips[j], self.clips[i]


# c1 = Clip('gangnam', 2012)
# print(c1)
# print(c1.is_player)
# c1.play()
# print(c1.is_player)
c2 = ArtClip('gangnam', 2012, 3)
# print(c2)
# print(c2.is_valid_for_euro())
# c3 = ArtClip('moon', 2001, 4)
# print(c3.is_valid_for_euro())
# my_list1 = range(0, 11, 2)
my_list ={0, 2, 4, 6, 8, 10}
# for i in range(0, 11, 2):
#     my_list.append(i)
# print(my_list)
# i=0
# while i < len(my_list):
#     my_list.pop(i)
#     i +=1
# print(my_list)
my_list.pop()
print(my_list)