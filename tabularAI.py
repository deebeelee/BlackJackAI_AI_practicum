# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:14:37 2018

@author: Arjun
Tabular AI
"""
import Player
import numpy as np
import csv

class tabularAI(Player.iPlayer):
    def __init__(self,money,name):
        super().__init__(money,name)
        data = list(csv.reader(open("blackjack_strategy_table.csv")))
        data[0][0] = '0'
        self.table = data

    def initial_bet(self):
        # Bets 90 % of whatever he has
        return 1

    def to_hit(self, game_state, player_hand):
        player_score = self.get_hand_score(player_hand)
        do_i_have_an_ace = (player_hand[0] != 0)
        # Now figure out what face up card the dealer has
        dealer_hand = game_state[60:73] # The first 13 boxes are one-hot encoded with the dealer's hand
        #print("This is the dealer hand.")
        #print(dealer_hand)
        dealer_face_up_card = -1
        for i in range(len(dealer_hand)):
            if(dealer_hand[i] == 1):
                dealer_face_up_card = i # This will always be one off the true value of the card
                break
        assert (dealer_face_up_card != -1)
        #print("This is the tabular AI. The dealer's face-up card is a", i)
        
        if(do_i_have_an_ace):
            # In this case, we use the soft-hand section to determine our decision
            index_to_start = 14
            if(player_score >= 21):
                return False
            elif(player_score <= 12):
                return True
            else:
                index_of_score = 34 - player_score
                #print("The tabular AI's score is %d, so it's index is %d",player_score,index_of_score)
                decision = self.table[int(index_of_score)][int(dealer_face_up_card)]
                if(decision == '0'):
                    return False
                else:
                    return True     
        else:
            # In this case, we can use the hard-hand section to determine the AI's decision
            index_to_start = 0
            if(player_score >= 18):
                return False
            else:
                index_of_score = 18 - player_score
                #print("The tabular AI's score is %d, so it's index is %d",player_score,index_of_score)
                decision = self.table[int(index_of_score)][int(dealer_face_up_card)]
                if(decision == '0'):
                    return False
                else:
                    return True
            
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