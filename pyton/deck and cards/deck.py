import random
from card import Card

class Deck:
    def __init__(self):
        self._deck = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        suits = ['Heart', 'Diamond', 'Club', 'Spade']
        names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for name in names:
                self._deck.append(Card(name, suit))
        self._deck.append(Card('Joker'))
        self._deck.append(Card('Joker'))

    def shuffle(self):
        random.shuffle(self._deck)

    def draw(self):
        return self._deck.pop(0)

    def __len__(self):
        return len(self._deck)

    def __getitem__(self, i):
        if i < len(self._deck):
            return self._deck[i]
        raise IndexError("Deck index out of range")

    def get_deck(self):
        return self._deck

    def sort_by_suit(self):
        self._deck.sort(key=lambda card: (card.suit, card._rank))

    def sort_by_rank(self):
        self._deck.sort(key=lambda card: (card._rank, card.suit))

    def deal_hand(self, num_cards):
        hand = [self.draw() for _ in range(num_cards)]
        return hand

    def count_cards(self):
        count = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0,
                 'K': 0, 'Joker': 0}
        for card in self._deck:
            count[card.value] += 1
        return count
