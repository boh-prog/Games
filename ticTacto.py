'''This program is a tic-tac-toe Game.
    It has two functions:
    printboard - that prints game board and
    playGame - that controls the gameplay
'''
#from IPython.display import clear_output
def printBoard(somedict):
    #clear_output()
    '''This function prints the game board; with values of a given dictionary parameter'''
    print(' | {0} | {1} | {2} |'.format(somedict['sv'],somedict['eght'],somedict['nin']) )
    print('-|' + '---|' + '---|' + '---|' )
    print(' | {0} | {1} | {2} |'.format(somedict['fr'],somedict['fv'],somedict['sx']) )
    print('-|' + '---|' + '---|' + '---|' )
    print(' | {0} | {1} | {2} |'.format(somedict['one'],somedict['tw'],somedict['th']) )

def rePlay(choice):
    '''Controls user decision to replay game'''
    if choice == 'yes':
        return playGame()
    else:
        print ('Thanks for playing')

        
def playGame():
    '''this function controls the actual gameplay'''
    print('This is a tic-tac-toe game.\nLets Play!!')
    
    cntPlays = 8 #keep track of moves by users (they have max of 8 moves: 4 for each)
    
    dict_nums = {1:'one',2:'tw',3:'th',4:'fr',5:'fv',6:'sx',7:'sv',8:'eght',9:'nin'}#this store string keys
                                                                                    #for the dict_play dict.
    dict_play = dict(zip(dict_nums.values(),(' '*9))) #stores values that are accessed and displayed.
                                                    #its keys are "values" in dict_nums. And all initial values are a whitespace
    
    printBoard(dict_play) #initially print board, by calling printBoard func:
                            #give it dict_play dictionary
    player1, player2, list_inputs = [], [], [] #store input from users + general list of inputs
    
    while cntPlays > 0:
        try:
            user_postn = int( input('input postion (1-9) >> ') )#get value for user position on bard: refer to numbers on key board numpad
        
            if not(user_postn in list_inputs):#if inputs are not repeated execute body of conditional
                list_inputs.append(user_postn) #add position played in list_inputs; keeping track so position can't be repeated
                
                #players play in rounds of even or odd; by count
                if cntPlays % 2 == 0: #first player has "X" values
                    
                    player1.append(user_postn) #keeping track of player1 positions to analyse alignment for a Game win
                    
                    #access value to display in dict_play, by getting key from dict_nums.
                    dict_play[ dict_nums[user_postn] ] = 'X' #change that position keyValue in dict_play to 'X'
                        
                    printBoard(dict_play) #print out board with updated "dic_play" dictionary
                    
                    cntPlays -= 1 #decrement cntPlays after each play
                        
                else:
                    dict_play[dict_nums[user_postn]] = 'O' #second player has "O" values

                    player2.append(user_postn) #update player2 list of plays too
                        
                    printBoard(dict_play) #print board with updated "dict_play" dictionary
                    
                    cntPlays -= 1

            #To win player must have at least three entries.
            #if the difference between number positions of all entries are thesame, then player wins
                    
            win_set = ([1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]) #set of all possible win plays
            
            if len(player1)==3 and sorted(player1) in win_set:
                choice = input('\nPlayer 1 wins!!! Bravo!Bravo!\n\nWant to Replay? (Yes or NO): ').lower()
                rePlay(choice)
                break
                    
            elif len(player2)==3 and sorted(player2) in win_set:
                choice = input('\nPlayer 2 wins!!! Bravo!Bravo!\n\nWant to Replay? (Yes or NO): ').lower()
                rePlay(choice)
                break
        except:
            pass
            
    else: #if there was no win while players played then its a Draw.
        print( 'Game is a Draw!!')
        
            
    
        
playGame()
