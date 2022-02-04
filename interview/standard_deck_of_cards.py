import random


class Card:
    # we have total 52 cards that contains 4 suits ie: Spades, Clubs, Diamonds, Hearts
    # for each suits we will have 13 cards, set of 4 suits is called deck
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    special_card_map = {
        1: 'Ace',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        """
        This function will show up a card
        """
        return print(f"{self.val} of {self.suit}")


class Deck:
    # a deck will contain 13 cards in each suits,
    # so total of 52 cards and 13 cards in each suits
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """
        This function will build deck of 52 cards for each suit
        """
        for s in Card.suits:
            for v in range(1, 14):
                if v in Card.special_card_map:
                    val = Card.special_card_map[v]
                else:
                    val = v
                self.cards.append(Card(s, val))

    def show(self):
        """
        This function will show-up all the deck cards
        """
        for c in self.cards:
            c.show()

    def shuffle_card(self):
        """
        This function will shuffle the cards
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        This function will get a card from the deck
        """
        return self.cards.pop()

    def group_cards(self, card_val):
        """
        This function will group on the value of card.
        eg like we will have 4 kings of each suite
        """
        if not card_val or (card_val not in list(range(2, 11)) and card_val not in list(Card.special_card_map.values())):
            print("Please provide card no from 2 to 10 or 'Ace' or 'Jack' or 'Queen' or 'King'")
            exit(0)

        cards = list(filter(lambda x: x.val == card_val, self.cards))
        for c in cards:
            c.show()

    def group_on_suits(self, suit_val):
        """
        This function will show all the cards for the specified suit,
        eg like we will have 13 cards in each suit
        """
        if not suit_val or suit_val not in Card.suits:
            print(f"Please provide suite value, choices are {Card.suits}")
            exit(0)
        cards = list(filter(lambda x: x.suit == suit_val, self.cards))
        for c in cards:
            c.show()


# deck = Deck()
# deck.show()
# deck.group_cards('King')
# deck.group_on_suits('Clubs')
# deck.shuffle_card()
# card = deck.draw_card()
# card.show()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        """
        This function will get a card from deck and put it into hand of a player
        and also return self so that we can chain it
        """
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        """
        This function will show up cards that are in hand of a player
        """
        for card in self.hand:
            card.show()


class App:
    def __init__(self):
        self.deck = Deck()  # create a deck of cards
        self.players = {}  # dictionary that will contains player object, dictionary is required as we need to
        # distribute card one at a time to each player, hence in 2nd or more iteration of distribution we need to lookup
        # for same Player object, so that we can have track of cards of a particular player in his hand

    def add_players(self, player_name):
        """
        This function will add a player
        """
        self.players[player_name] = Player(player_name)

    def deal_cards(self, distribute_to_each=4):
        """
        This function will distribute cards to each player clockwise or anticlockwise
        distribute_to_each: we can pass how much no of cards a player should hold in his hand
        """
        self.deck.shuffle_card()  # shuffle the deck cards before distribution
        # start distribution
        while distribute_to_each > 0:
            for player_name in self.players.keys():
                self.players[player_name] = self.players[player_name].draw_card(self.deck)
            distribute_to_each -= 1

    def show_cards(self, player_name):
        """
        This function will track of the cards in a player's hand
        """
        self.players[player_name].show_hand()


app = App()
player_names = ['Himanshu', 'Ashutosh', 'Sai', 'Vaibhav']
for p in player_names:
    app.add_players(p)
app.deal_cards()

print("Player1 cards - ******************")
app.show_cards('Himanshu')
print("Player2 cards - ******************")
app.show_cards('Ashutosh')
print("Player3 cards - ******************")
app.show_cards('Sai')
print("Player4 cards - ******************")
app.show_cards('Vaibhav')

print(f"Remaining cards on the floor - {len(app.deck.cards)}")
