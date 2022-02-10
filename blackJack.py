class Card:
    '''buildcard objects'''
    ##every card object have ranking and alliance2666
    ##
    def __init__(self, rank, alliance, value):
        self.rank = rank 
        self.alliance = alliance ##
        self.value = value ##card numeric value
        
 
import random
class Deck:
    '''creates a collectioin of card objects'''
    ##a deck consist of card objects
    def __init__(self):
        self.deck = [] 
        for alliance in ["black","heart","clover","spades"]:
            ##create of list of card objects: 52cards
            self.deck.append(Card("A",alliance,[1,11]))##value for "A" is either 1 or 11
            self.deck.append(Card('2',alliance,2))
            self.deck.append(Card('3',alliance,3))
            self.deck.append(Card('4',alliance,4))
            self.deck.append(Card('5',alliance,5))
            self.deck.append(Card('6',alliance,6))
            self.deck.append(Card('7',alliance,7))
            self.deck.append(Card('8',alliance,8))
            self.deck.append(Card('9',alliance,9))
            self.deck.append(Card('10',alliance,10))
            self.deck.append(Card("Joker",alliance,10))
            self.deck.append(Card("Queen",alliance,10))
            self.deck.append(Card("King",alliance,10))
        
    def shuffle(self):
        '''shuffle the deck of cards'''
        random.shuffle(self.deck) ##shuffle deck of cards
        
        
        
        class Player:
    def __init__(self, playerName): ##two players, dealer and player1
        self.name = playerName
        self.cards = []##cards the player has in hand
        
    def drawCard(self, deck): ##deck is array of cards on deck
        '''draws card from deck'''
        #self.cards.append()
        self.cards.append(deck.pop())
        
    def playcard(self): ##not needed in blackJack
        '''return card from player's set '''
        return self.cards.pop()##play a card from player's set
    
    def sumValue(self):
        cardValues = [] ##list of card values
        ace_in_cards = False
        for card in self.cards:
            if type(card.value) == int:
                cardValues.append(card.value)
            else: ##and Exception for the Ace card, which is a list of two Values
                ace_in_cards = True
                ##val_1 is a ONE and val_11 is an ELEVEN
                val_1, val_11 = card.value[0], card.value[1] ##get the values in 
                
        ##
        if ace_in_cards: return (sum(cardValues)+val_1, sum(cardValues)+val_11)##two possible sumValue of cards if 'ace' in list
        else: return sum(cardValues)
    
    def getInitialCard(self,cards):##cards is list of cards given
        self.cards.extend(cards)
        
        
        
 ##class Play():
def PlayGame():
    player1 = Player(input("enter your name Player1: "))
    Dealer = Player("Dealer")
    DECK = Deck() ##create deck object
    DECK.shuffle()##shuffle cards
    deck = DECK.deck ##assing array of cards in DECK Object to deck variable
    ##give player 2 cards
   
    ##--------------------------------------
    
    def checkSumValue(player):
        sumValue = player.sumValue()
        ##checking sumValue to return the best value less than 21.
        if type(sumValue)==tuple:
            if max(sumValue)<=21: ##return maximum number in tuple that's still less than or equal to 21.
                return max(sumValue)
            elif min(sumValue)<=21: ##else return the minimum value if less than 21
                return min(sumValue)
            else: ##return any, since both values are greater than 21
                return sumValue[0]
            
        return sumValue
        
    
    def playTurn(player):##'player' can either be dealer or player1
        
        if player.name != 'Dealer':
            while checkSumValue(player)<=21:
                playerChoice = input(f"{player.name}, you have {checkSumValue(player)}\n Input 'D' to draw from deck or 'C' to cancel: ").upper()
                if playerChoice == "D":
                    player.drawCard(deck) ##add a card from deck to player1 set
                    #print(f"!!!!! {checkSumValue(player)} !!!")
                    if checkSumValue(player)==21: return "wins"
                    elif checkSumValue(player)>21: return "lose"
                elif playerChoice == "C":##player passes his turn
                    return 'pass'
            else: return 'lose'
        else:##dealer playing
            while checkSumValue(player)<=21:
                if checkSumValue(player)<15:
                    player.drawCard(deck)
                    ##checks! when ever a player draws from deck
                    if checkSumValue(player)==21: return "wins"
                    elif checkSumValue(player)>21: return "lose"
                else: 
                    option = random.randint(0,1) ##randomize the option for 'dealer'(CPU) to draw from deck
                    if option==1:
                        player.drawCard(deck)
                        if checkSumValue(player)==21: return "wins"
                        elif checkSumValue(player)>21: return "lose"
                    else: return 'pass'
            else: return 'lose'
    ##------------------------------------------
    
    while True:
        player1Play = playTurn(player1)##get results of player1's play
        ##-----------------------------
        ## print(f'Player1 total is {checkSumValue(player1)}')
        ## print(f'dealers total is {checkSumValue(Dealer)}')
        ##-----------------------------
        if player1Play == 'wins': return f"{player1.name} Wins with {checkSumValue(player1)}"
        elif player1Play == 'lose': return f"{Dealer.name} Wins with {checkSumValue(Dealer)}"
        
        else:##Dealer's turn to play
            dealerPlay = playTurn(Dealer) ##get results of Dealer's play
            ##-----------------------------
            ## print(f'dealers total is {checkSumValue(Dealer)}')
            ## print(f'Player1 total is {checkSumValue(player1)}')
            ##-----------------------------
            if dealerPlay == 'wins': return f"{Dealer.name} Wins with {checkSumValue(Dealer)} total card value"
            elif dealerPlay == 'lose': return f"{player1.name} Wins with {checkSumValue(player1)} total card value"
    
    
