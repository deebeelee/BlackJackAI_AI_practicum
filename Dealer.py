import Player
import numpy as np

class Dealer(Player.iPlayer):
    def __init__(self,money, name = "Arjun"):
        self.name = name
        self.money = money
        self.game_state = None
    def initial_bet(self):
        return 0 
    def to_hit(self, game_state, player_hand):
        self.game_state = game_state
        toHitOrNotToHit = np.random.rand(1)
        if(toHitOrNotToHit < 0.5):
            return True
        else:
            return False
    def print_game_state(self,game_state):
        pass
    def get_state(self):
        return self.game_state
        pass