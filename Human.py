# For AI Practicum.

import Player

class Human(Player.iPlayer):
    def __init__(self, money, name='lowly human', cards, others, profile):
        """ A Player has a name and a certain capital. They will know what
            cards they have revealed, and what others' cards are revealed.
            profile is the PlayerProfile for AI handling."""

        self.name = str(name)
        self.money = money
        # The following fields were initialized as fields here so that
        # the player has enough information without having access to the full game state.
        # That implies the Game Controller would have to update the player fields.
        self.cards = cards
        self.others = others
        self.profile = profile

    def get_state():
        """returns a summary of the state visible to this player."""
        pass

    def print_game_state():
        """prints the state visible to this player."""
        s = self.get_state()

    def initial_bet():
        """prompts human player for initial bet, return integer."""
        while True:
            ans = input('How much do you want to bet?')
            if not ans.isdigit():
                print('That\'s not real money!')
            else:
                bet = int(ans)
                if bet>self.money:
                    print('You cannot bet over what you have!')
                else:
                    self.money-=bet
                    return bet
    
    def to_hit(state, hand):
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
                print("Sorry, I'm afraid I cannot do that...because I don't understand.")