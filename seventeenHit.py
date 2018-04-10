"""
This AI hits until its score is 17. 
"""
import Player
import numpy as np

class seventeenHits(Player.iPlayer):
    def __init__(self,money,name = "Mitchel"):
        super().__init__(money,name)

    def initial_bet(self):
        # Bets 80 % of whatever he has
        return 0.8*self.money

    def to_hit(self, game_state, player_hand):
        if(self.get_hand_score(player_hand) < 17):
            return True
        else:
            return False

    def print_game_state(self,game_state):
        pass
      
    def get_state(self):
        pass
    def get_hand_score(self,player_hand):
        score = 0
        for i,v in enumerate(player_hand):
            if i == 0:
                score += v
            elif i >= 10:
                score += 10*v
            else:
                score += (i+1)*v
        return score
