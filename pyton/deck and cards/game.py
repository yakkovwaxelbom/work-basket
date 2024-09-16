from deck import Deck
from player import Player

class Game:
    def __init__(self, player_1='player_1', player_2='player_2'):
        self.winner = False
        self.deck = Deck()
        self.player_1 = Player(player_1, hand=self.deck.deal_hand(26))
        self.player_2 = Player(player_2, hand=self.deck.deal_hand(26))

    def receive_and_take_cards(self, win_player_1, i=0, j=0):
        if win_player_1:
            for _ in range(j):
                self.player_1.hand.append(self.player_2.hand.pop(0))
                self.player_1.hand.append(self.player_1.hand.pop(0))
            self.player_1.score += j
        else:
            for _ in range(i):
                self.player_2.hand.append(self.player_1.hand.pop(0))
                self.player_2.hand.append(self.player_2.hand.pop(0))
            self.player_2.score += i

    def war(self):
        i = 3
        try:
            while self.player_1.hand[i] == self.player_2.hand[i]:
                i += 3
            self.play_round(i, i)
        except IndexError:
            if len(self.player_1.hand) - 1 > i > len(self.player_2.hand) - 1:
                self.play_round(i, len(self.player_2.hand) - 1, True)
            elif len(self.player_2.hand) - 1 > i > len(self.player_1.hand) - 1:
                self.play_round(len(self.player_1.hand) - 1, i, True)
            else:
                self.play_round(len(self.player_1.hand) - 1, len(self.player_2.hand) - 1, True)

    def play_round(self, i=0, j=0, draw_war=False):
        if self.player_1.hand[i] > self.player_2.hand[j]:
            self.receive_and_take_cards(True, j=j + 1)
        elif self.player_1.hand[i] < self.player_2.hand[j]:
            self.receive_and_take_cards(False, i=i + 1)
        elif self.player_1.hand[i] == self.player_2.hand[j] and not draw_war:
            self.war()
        else:
            self.winner = True

    def get_winner(self):
        if len(self.player_1.hand) == 0 or len(self.player_2.hand) == 0:
            self.winner = True

    def play(self, rounds=100):
        for j in range(rounds):
            self.get_winner()
            if self.winner:
                break
            self.play_round()
            print(f'Round {j + 1} -------------------------')
            print(f'{self.player_1.name}: {self.player_1.hand}')
            print(f'{self.player_2.name}: {self.player_2.hand}')

        if self.player_1.score > self.player_2.score:
            print(f'{self.player_1.name} wins!')
        elif self.player_1.score < self.player_2.score:
            print(f'{self.player_2.name} wins!')
        else:
            print('Draw: The motley programmer is lost on you')

if __name__ == '__main__':
    a = Game('yakov', 'shloimy')
    a.play(1000)
