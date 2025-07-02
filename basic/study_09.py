import random
from enum import Enum


class Suite(Enum):
    '''花色枚举'''
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    '''牌'''

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        '''魔术方法或双下方法，定义对象的官方字符串表示形式'''
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value
    



class Poker:
    '''扑克牌'''

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        '''洗牌'''
        self.current = 0
        random.shuffle(self.cards)

    def deaf(self):
        '''发牌'''
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        '''还有没有牌可以发出去'''
        return self.current < len(self.cards)


class Player:
    '''玩家'''

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        '''摸牌'''
        self.cards.append(card)

    def arrange(self):
        '''整理手上的牌'''
        self.cards.sort()


if __name__ == '__main__':
    for suite in Suite:
        print(f'{suite}:{suite.value}')

    # 测试card类
    card1 = Card(Suite.HEART, 5)
    card2 = Card(Suite.SPADE, 10)
    print(card1)
    print(card2)

    poker = Poker()
    print(poker.cards)
    poker.shuffle()
    print(poker.cards)

    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get_one(poker.deaf())

    for player in players:
        player.arrange()
        print(f'{player.name}:', end='')
        print(player.cards)
