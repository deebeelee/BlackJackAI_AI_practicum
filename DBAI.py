import Player
import numpy as np

def score_hand(hand):
    score = 0
    num_aces = 0
    for i, v in enumerate(hand):
        if i == 0:
            num_aces = v
            score += v
        elif i >= 10:
            score += 10 * v
        else:
            score += (i+1) * v

    while(score < 12 and num_aces > 0):
        score += 10
        num_aces -= 1
    if(score > 21):
        score = -1
    elif(np.sum(hand) == 5 and score <= 21):
        score = 22
    if(score == 21 and np.sum(hand) == 2):
        score = 23
    return score

class DBAI(Player.iPlayer):
    """Represents a slightly less dumb AI that looks at its own hand and
       becomes less likely to hit as the scores approaches 21."""
    def __init__(self,money,name):
        super().__init__(money,name)

    def initial_bet(self):
        # Bets 50 % of whatever he has
        return 0.5*self.money

    def to_hit(self, game_state, player_hand):
        score = score_hand(player_hand)
        # decide probabilistically only if it is possible to bust
        # naively assume infinite number of cards
        if score >= 21: return False
        if score <= 10: return True
        fail = 21-score
        # Face cards, and number cards counted separately.
        failcards = (1 if fail<10 else 0)*3 + (10 - fail)
        p_fail = float(failcards)/13
        return np.random.rand(1) > p_fail

    def print_game_state(self,game_state):
        pass
        
    def get_state(self):
        pass