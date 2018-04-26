import Player
import numpy as np

class dumbAI(Player.iPlayer):
    def __init__(self,money,name):
        super().__init__(money,name)

    def initial_bet(self):
        # Bets 50 % of whatever he has
        return 0.5*self.money

    def to_hit(self, game_state, player_hand):
        toHitOrNotToHit = np.random.rand(1)
        if(toHitOrNotToHit < 0.5):
            return True
        else:
            return False

    def print_game_state(self,game_state):
        pass
        
    def get_state(self):
        pass