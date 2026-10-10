import random
# GLOBAL VARIABLES FOR CARDS' SUITS, RANKS, VALUES
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# CARD CLASS:
# Every card has a suit, rank, and value.
class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return self.rank + " of " + self.suit

# DECK CLASS:
# This will instantiate a new deck of 52 cards 
# (All objects in a list)
# And also shuffle the deck through a method call
# AND also deal cards from the deck object (Popping from cards list)

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # This is where the card objects are created and appended to the list
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

        print("Deck has been shuffled!")

    def deal_one(self):
        return self.all_cards.pop()

# PLAYER CLASS:
# Will be used to 'hold' a player's list of cards.
# Should be able to add/remove cards from that player's hand.

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        # Multiple cards to be added
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)

        # One card to be added
        else:
            self.all_cards.append(new_cards)

    def number_cards(self):
        return len(self.all_cards)

    def __str__(self):
        return(f'Player {self.name} has {len(self.all_cards)} card(s).')

# ACTUAL GAME LOGIC
# We first have to create two instances of the player class, player 1 and 2.
# Each player has a shuffled half of a deck that we also instantiate.
# Repeatedly check for 0 cards. If not, we play another round.
# Each round, we compare each player's dealt card. 
# The player with the better card wins both cards.
# When war happens (Two of the same card value):
# we deal three cards, then compare another card.
# We do this repeatedly until one player wins all the cards, extending their list.
# This happens until one player has zero cards.
# We count the amount of round that have happened.

p1 = Player("1")
p2 = Player("2")
theDeck = Deck()
theDeck.shuffle()
for i in range(26):
    p1.add_cards(theDeck.deal_one())
    p2.add_cards(theDeck.deal_one())
game_on = True
round_count = 0
MAX_ROUNDS = 100000
# If a winner isn't determined in 100k rounds, automatically end the game (Should never be the case, but just in case)

while game_on == True:

    if round_count > MAX_ROUNDS:
        print(f'Game declared a draw after {MAX_ROUNDS} rounds (infinite loop detected)!')
        game_on = False
        break
    if len(p1.all_cards) == 0:
        print(f'Player 2 wins in {round_count} rounds!')
        game_on = False
        break
    elif len(p2.all_cards) == 0:
        print(f'Player 1 Wins in {round_count} rounds!')
        game_on = False
        break

    p1_current_cards = []
    p2_current_cards = []
    p1_current_cards.append(p1.remove_one())
    p2_current_cards.append(p2.remove_one())
    round_count += 1

    at_war = True
    
    while at_war:

        if p1_current_cards[-1].value > p2_current_cards[-1].value:
            print("Player 1 wins this round!")
            print(p1)
            rint = random.randint(0,1)
            if rint == 0:
                p1.add_cards(p1_current_cards)
                p1.add_cards(p2_current_cards)
            if rint == 1:
                p1.add_cards(p2_current_cards)
                p1.add_cards(p1_current_cards)

            at_war = False
            break
        elif p1_current_cards[-1].value < p2_current_cards[-1].value:
            print("Player 2 wins this round!")
            print(p2)
            rint = random.randint(0,1)
            if rint == 0:
                p2.add_cards(p2_current_cards)
                p2.add_cards(p1_current_cards)
            if rint == 1:
                p2.add_cards(p1_current_cards)
                p2.add_cards(p2_current_cards)
            at_war = False
            break
        else:
            print("War!")

            if len(p1.all_cards) < 3:
                print("Player 1 is unable to play war! Game over!")
                print(f'Player 2 wins in {round_count} rounds!')
                game_on = False
                at_war = False
                break
            elif len(p2.all_cards) < 3:
                print("Player 2 is unable to play war! Game over!")
                print(f'Player 1 wins in {round_count} rounds!')
                game_on = False
                at_war = False
                break

            else:
                for i in range (3):
                    p1_current_cards.append(p1.remove_one())
                    p2_current_cards.append(p2.remove_one())