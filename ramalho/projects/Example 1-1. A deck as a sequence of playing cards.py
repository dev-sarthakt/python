import collections

Card=collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:

    ranks=list(str(i) for i in range(2, 11))+list("JQKA")
    suits="spades diamonds clubs hearts".split()

    def __init__(self):
        self._card=[Card(rank, suit) for rank in self.ranks for suit in self.suits]

if __name__=="__main__":
    fd=FrenchDeck()
    suit_val=dict(spades=3, hearts=2, diamonds=1, clubs=0)
    
    def spades_high(card):
        rank_val=fd.ranks.index(card.rank)
        return rank_val*4+suit_val[card.suit]
    
    for card in sorted(fd._card, key=spades_high):
        print(card)