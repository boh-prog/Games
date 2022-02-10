## War Game
## ver1

import random

class Card:
    '''build card object'''
    ##every card object have ranking and alliance2666
    def __init__(self, rank, alliance, value):
        self.rank = rank 
        self.alliance = alliance ##
        self.value = value ##card numeric value
        
    def __repr__(self):
        return f"{self.rank}{self.alliance}"



class Deck:
    '''creates a collectioin of card objects'''
    ##a deck consist of card objects
    def __init__(self):
        self.deck = []
        for alliance in ["black","heart","clover","spades"]:
            ##create of list of card objects: 52cards
            self.deck.append(Card("A",alliance,14))
            self.deck.append(Card('2',alliance,2))
            self.deck.append(Card('3',alliance,3))
            self.deck.append(Card('4',alliance,4))
            self.deck.append(Card('5',alliance,5))
            self.deck.append(Card('6',alliance,6))
            self.deck.append(Card('7',alliance,7))
            self.deck.append(Card('8',alliance,8))
            self.deck.append(Card('9',alliance,9))
            self.deck.append(Card('10',alliance,10))
            self.deck.append(Card("Joker",alliance,11))
            self.deck.append(Card("Queen",alliance,12))
            self.deck.append(Card("King",alliance,13))
        
    def shuffle(self):
        '''shuffle the deck of cards'''
        random.shuffle(self.deck) ##shuffle deck of cards
    def __len__(self):
        return len(self.deck)
    def pop(self):
        return self.deck.pop()


class Player:
    ''' defines the player object
        Each player has a name and hold a set of cards
    '''
    def __init__(self, playerName):
        self.name = playerName
        self.cards = []##cards up
        self.faceDown = []
        self.faceUp = []
        
    def playCard(self):
        '''return card from player's set '''
        if self.faceDown:
            return self.faceDown.pop()##play a card from player faceDown deck
        elif self.faceUp:
            ##faceUp cards to faceDown Deck and suffle
            self.addCards(self.faceUp, "down")
            self.shuffle()
            return self.faceDown.pop()
    def shuffle(self):
        '''shuffles card in faceDown deck'''
        random.shuffle(self.faceDown)
    def addCards(self, arrayOfCards, deck=None):
        if deck == 'down':##add cards to player deck of faceDown cards
            self.faceDown = self.faceDown + arrayOfCards
        else: ##add win cards to players deck of win plays
            self.faceUp = self.faceUp + arrayOfCards
    def countCards(self):
        ##count total number of cards player holds
        return len(self.faceDown + self.faceUp)
    
    def __repr__(self):
        return f"name {self.name}\n cards {self.cards}"
    
    
def Board(player1, player2, card1, card2, warCards):
    '''compare the cards played on baord'''
    if card1.value > card2.value:
        cards = [card1,card2] + warCards
        player1.addCards(cards)
    elif card1.value < card2.value: 
        cards = [card1,card2] + warCards
        player2.addCards(cards)
    else: 
        return "tie"
def shareCards(player1, player2, deck):
    deck = deck.deck
    set1, set2 = [], []
    for c in range(len(deck)-1): ##distribute cards to players, 26 cards each
        set1.append(deck[c])
        set2.append(deck[c+1])
    player1.addCards(set1)
    player2.addCards(set2)


def PlayGame(): 
    
    player1 = Player(input("Enter name of player1: ")) ##get name of player 1
    player2 = Player(input("Enter name of player2: ")) ##get name of player 2
    
    Dk = Deck() ## get deck of cards
    Dk.shuffle() ## shuffle cards
    warCards = [] ##instantiate cards resulting from warPlay
    
    shareCards(player1, player2, Dk) ##distribute cards to players
    
    while True:
        
        if player1.countCards() == 52:
            return f"{player1.name} Wins!"
        elif player2.countCards()==52:
            return f"{player2.name} Wins!"
        
        ##check case when player does not have cards to play and the other does not have 52 cards
        elif player1.countCards()==0: 
            return f"{player2.name} Wins!"
        elif player2.countCards()==0: 
            return f"{player1.name} Wins!"
        
        ##proceed to playe
        card1 = player1.playCard()
        card2 = player2.playCard()
        
        print(card1.value,card2.value) ##debugging purpose
        
        if Board(player1, player2, card1, card2, warCards) == "tie":
            ##players play faceDown Cards from their deck
            ##check if each player still has cards to play
            if player1.countCards()==0: 
                return f"{player2.name} Wins!"
            elif player2.countCards()==0:
                return f"{player1.name} Wins!"
            downCard1, downCard2 = player1.playCard(), player2.playCard()
            warCards = warCards + [card1, card2, downCard1, downCard2] ##add cards resulting from war play to War Deck
            ##proceed to next play
        
