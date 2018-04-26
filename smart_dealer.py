import Player
import numpy as np

class SmartDealer(Player.iPlayer):
    def __init__(self, model):
        super().__init__(money,name)
        self.model = model
    def initial_bet(self):
        return 0 
    def to_hit(self, game_state, player_hand):
        return model.activate(np.concatenate((game_state, player_hand))) >= 0
    def print_game_state(self,game_state):
        pass
    def get_state(self):
        return self.game_state
        pass