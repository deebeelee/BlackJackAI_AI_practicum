# For AI Practicum.

import Player

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
                if bet>self.money:
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
                self.print_game_state()
            elif ans in ['hit','"hit"','h']:
                return True
            elif ans in ['fold','"fold"','f']:
                return False
            else:
                print("Sorry, I'm afraid I cannot do that...because I don't understand.\n")

    def print_game_state(self, game_state):
        """prints the state visible to this player."""
        pass

    def get_state(self):
        """returns a summary of the state visible to this player."""
        pass