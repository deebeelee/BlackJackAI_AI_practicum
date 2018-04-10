import numpy as np
import random

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

	def deal(self, player):
		card = random.choice(np.nonzero(self.deck)[0])
		self.deck[card] = 0
		self.hands[player.get_id()][card%13] += 1
		if(not (player.get_id() in self.visible)):
			self.visible[player.get_id()] = self.hands[player.get_id()].copy()

	def play_game(self):
		self.bets = {}
		for player in self.players:
			self.bets[player.get_id()] = player.initial_bet()

		for player in self.players:
			self.deal(player)
			self.deal(player)
		self.deal(self.dealer)
		self.deal(self.dealer)
		for player in self.players:
			while(np.sum(self.hands[player.get_id()]) < 5 and player.to_hit(self.get_state(), self.hands[player.get_id()])):
				self.deal(player)
		while(np.sum(self.hands[self.dealer.get_id()]) < 5 and self.dealer.to_hit(self.get_state(), self.hands[player.get_id()])):
			self.deal(self.dealer)

	def get_state(self):
		state = np.empty(15 * len(self.players) + 14)
		for i, player in enumerate(self.players):
			player_start = 15*i
			state[player_start:player_start+13] = self.visible[player.get_id()]
			state[player_start+13] = np.sum(self.hands[player.get_id()]) - 1
			state[player_start+14] = self.bets[player.get_id()]
		dealer_start = 15 * len(self.players)
		state[dealer_start:dealer_start+13] = self.visible[self.dealer.get_id()]
		state[dealer_start+13] = np.sum(self.hands[self.dealer.get_id()]) - 1
		return state

	def print_game(self):
		print('Deck status')
		print(self.deck)
		for player in self.players:
			print('Player %s \'s cards' % player.get_id())
			print(self.hands[player.get_id()])
		print('Dealer\'s hand')
		print(self.hands[self.dealer.get_id()])

 