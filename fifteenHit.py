"""
This AI hits until its score is 15. 
"""
import Player
import numpy as np

class fifteenHits(Player.iPlayer):
    def __init__(self,money,name = "Mitchel"):
        super().__init__(money,name)

    def initial_bet(self):
        # Bets 80 % of whatever he has
        return 0.8*self.money

    def to_hit(self, game_state, player_hand):
        if(self.get_hand_score(player_hand) < 15):
            return True
        else:
            return False

    def print_game_state(self,game_state):
        pass
    
    def get_hand_score(self,player_hand):
        score = 0
        for k in range(13):
            if(player_hand[k] == 1):
                score += (k+1)
        return score
        
    def get_state(self):
        pass
"""

