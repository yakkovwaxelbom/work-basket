class Player:
    def __init__(self, name, hand: list):
        self.name = name
        self.hand = hand
        self.score = 0

    def __str__(self):
        return str(self.name)

    def __len__(self):
        return len(self.hand)
