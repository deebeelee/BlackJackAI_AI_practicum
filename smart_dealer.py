import Player
import numpy as np

class SmartDealer(Player.iPlayer):
    def __init__(self, model, name):
        super().__init__(0, name)
        self.model = model
    def initial_bet(self):
        return 0 
    def to_hit(self, game_state, player_hand):
        return self.model.activate(np.concatenate((game_state, player_hand)))[0] >= 0.5
    def print_game_state(self,game_state):
        pass
    def get_state(self):
        return self.game_state
        pass