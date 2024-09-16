class Card:
    def __init__(self, value: str, suit=None):
        self._rank = None
        self._suit = suit
        self.value = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        suits = ['Heart', 'Diamond', 'Club', 'Spade']
        if suit in suits:
            self._suit = suit
        else:
            raise ValueError("Invalid suit")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        if value == 'Joker':
            self._value = 'Joker'
            self._suit = 'x'  # Joker is forced to the end of the deck when sorting
        elif value in names:
            self._value = value
            ranks = {'A': 13, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11,
                     'K': 12, 'Joker': float('inf')}
            self._rank = ranks[value]
        else:
            raise ValueError("Invalid card value")

    def __lt__(self, other):
        if self.suit == other.suit:
            return self._rank < other._rank
        raise NotImplementedError("Cannot compare cards with different suits")

    def __str__(self):
        return f'({self.value},{self.suit})'

    def __repr__(self):
        return self.__str__()
