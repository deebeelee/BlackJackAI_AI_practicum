import numpy as np
import random

class BlackjackGame():

	def __init__(self, player_list, dealer):
		self.deck = np.ones(52)
		self.players = player_list
		self.dealer = dealer
		self.visible = {}
		hands = {}
		bets = {}
		for player in player_list:
			hands[player.get_id()] = np.zeros(13)
			bets[player.get_id()] = player.initial_bet()
		hands[dealer.get_id()] = np.zeros(13)
		self.hands = hands

	def check_wins(self):
		dealer_score = score_hand(self.hands[self.dealer.get_id()])
		wins = np.zeros(len(self.players))
		for i, player in enumerate(self.players):
			score = score_hand(self.hands[player.get_id()])
			if(score == dealer_score):
				wins[i] = -1
			elif(score > dealer_score):
				wins[i] = 1
		return wins

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

		while(score <= 12 and num_aces > 0):
			score += 9
			num_aces -= 1
		if(score > 21):
			score = -1
		elif(np.sum(hand) == 5 and score <= 21):
			score = 22
		return score

	def deal(self, player):
		card = random.choice(np.nonzero(self.deck))
		self.deck[card] = 0
		self.hand[player.get_id()][card%13] += 1
		if(not (player.get_id() in self.visible)):
			self.visible[player.get_id()] = card%13

	def play_game(self):
		self.bets = []
		for player in self.player_list:
			self.bets.append(player.initial_bet())

		for player in self.player_list:
			deal(self, player)
			deal(self, player)
		for player in self.player_list:
			while(np.sum(self.hands[player.get_id()]) < 5 and player.to_hit()):
				deal(self, player)
		while(np.sum(self.hands[dealer.get_id()]) < 5 and dealer.to_hit()):
			deal(self, dealer)

	def get_state(self):
		state = np.empty(3 * len(player_list) + 2)
		for i, player in enumerate(self.player_list):
			state[i] = self.visible[player.get_id()]
			state[i+1] = np.sum(self.hands[player.get_id()]) - 1
			state[i+2] = self.bets[player.get_id()]
		dealer_start = 3 * len(player_list)
		state[dealer_start] = self.visible[self.dealer.get_id()]
		state[dealer_start + 1] = np.sum(self.hands[self.dealer.get_id()])
		return state

	def print_game():
		for player in self.player_list:
			print('Player %s \'s cards')
			print(np.where(self.hands[player.get_id()]))

 