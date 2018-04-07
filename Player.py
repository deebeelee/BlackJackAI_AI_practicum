from abc import ABC, abstractmethod
import numpy as np
import uuid

class iPlayer(ABC):
    def __init__(self, money, name = "Mitchel Fung"):
        self.name = name
        self.money = money
        self.id = str(uuid.uuid4()) 
    @abstractmethod
    def initial_bet(self):
        pass
    def to_hit(self, game_state, player_hand):
        pass
    def print_game_state(self,game_state):
        pass
    def get_state(self):
        pass
    def get_id(self):
        return self.id