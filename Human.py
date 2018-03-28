# For AI Practicum.

import Player
import numpy as np

class Human(Player.iPlayer):
    def __init__(self, money, name='lowly human'):
        """ An instance of a human player."""
        super().__init__(money,name)

    def initial_bet(self):
        """prompts human player for initial bet, return integer."""
        while True:
            ans = input('How much do you want to bet?\n')
            if not ans.isdigit():
                print('That\'s not real money!')
            else:
                bet = int(ans)
                if bet> self.money:
                    print('You cannot bet over what you have!')
                else:
                    self.money-=bet
                    return bet
    
    def to_hit(self, game_state, player_hand):
        """ Returns True if the player hits, False otherwise."""
        while True:
            print('Choose your action from below:\n\n'+
                  '- "hit"   or   "fold"\n' + 
                  '- "look" to see the game state.\n')
            ans = str(input())
            if ans in ['look','"look"','l']:
                self.print_game_state(game_state)
                self.print_hand(player_hand)
            elif ans in ['hit','"hit"','h']:
                return True
            elif ans in ['fold','"fold"','f']:
                return False
            else:
                print("Sorry, I'm afraid I cannot do that...because I don't understand.\n")

    def print_game_state(self, game_state):
        """prints the state visible to this player."""
        # This is a 3x5 array 
        tabular_game_state = np.resize(game_state,(5,3))
        print("Here is some metadata about the current game state.")
        print("Visible cards are marked as V, the number of hidden cards as N,")
        print("and the initial bet for a given player as B.")
        print("\n")
        print("V | N | B")
        for i in range(5):
            for j in range(3):
                print(tabular_game_state[i][j], end = ' | ')
            print("\n")

    def get_state(self):
        """returns a summary of the state visible to this player."""
        pass
    
    def convert_array_to_hand(self,card_no):
        """ This converts a card number to a string."""
        if(card_no == 0):
            return "Ace"
        elif(card_no == 1):
            return "Two"
        elif(card_no == 2):
            return "Three"
        elif(card_no == 3):
            return "Four"
        elif(card_no == 4):
            return "Five"
        elif(card_no == 5):
            return "Six"
        elif(card_no == 6):
            return "Seven"
        elif(card_no == 7):
            return "Eight"
        elif(card_no == 8):
            return "Nine"
        elif(card_no == 9):
            return "Ten"
        elif(card_no == 10):
            return "Jack"
        elif(card_no == 11):
            return "Queen"
        elif(card_no == 12):
            return "King"
    
    def print_hand(self, player_hand):
        """ This prints the player's hand. """
        your_hand = "You have:\n"
        for i in range(len(player_hand)):
            if(player_hand[i] != 0 ):
               if([player_hand[i] == 1]):
                   your_hand += "1 " + self.convert_array_to_hand(i) + "\n"
               else:
                   your_hand += ", " + str(player_hand[i]) + self.convert_array_to_hand(i) + "s\n"
        print(your_hand)