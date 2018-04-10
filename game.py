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

#number of games
#average hand size
#average bet
#average score
#bustrate
#winrate
class Profile():
	def __init__(self):
		self.num_games = 0
		self.total_cards = 0
		self.total_bets = 0
		self.total_score = 0
		self.busts = 0
		self.wins = 0

	def add_game(self, hand_size, bet, score, bust, won):
		self.num_games += 1
		self.total_cards += hand_size
		self.total_bets += bet
		self.total_score += score
		self.busts += bust
		self.wins += won

	def get_stats(self):
		stats = -np.ones(6)
		stats[0] = self.num_games
		if self.num_games == 0:
			return stats
		else:
			stats[1] = self.total_cards/self.num_games
			stats[2] = self.total_bets/self.num_games
			if not (self.num_games == self.busts):
				stats[3] = self.total_score/(self.num_games - self.busts)
			stats[4] = self.busts/self.num_games
			stats[5] = self.wins/self.num_games
		return stats

class BlackjackGame():

	def __init__(self, player_list, dealer):
		self.deck = np.ones(52)
		self.players = player_list
		self.dealer = dealer
		self.dealer_profit = 0
		self.visible = {}
		hands = {}
		bets = {}
		profiles = {}
		for player in player_list:
			hands[player.get_id()] = np.zeros(13)
			profiles[player.get_id()] = Profile()
		hands[dealer.get_id()] = np.zeros(13)
		self.hands = hands
		self.profiles = profiles

	def check_wins(self):
		dealer_score = score_hand(self.hands[self.dealer.get_id()])
		wins = np.zeros(len(self.players))
		for i, player in enumerate(self.players):
			score = score_hand(self.hands[player.get_id()])
			
			if(score < dealer_score):
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
		wins = self.check_wins()
		#update player profiles
		for i, player in enumerate(self.players):
			player_profile = self.profiles[player.get_id()]
			hand = self.hands[player.get_id()]
			score = score_hand(hand)
			bust = False
			if(score == -1):
				score = 0
				bust = True
			player_profile.add_game(np.sum(hand), self.bets[player.get_id()], score, bust, wins[i])
		self.get_profit(wins)

	def clear_game(self):
		for player in self.players:
			self.bets[player.get_id()] = 0
			self.hands[player.get_id()] = np.zeros(13)

	def get_state(self):
		state = np.empty(15 * len(self.players) + 14)
		for i, player in enumerate(self.players):
			player_start = 15*i
			state[player_start:player_start+13] = self.visible[player.get_id()]
			state[player_start+13] = np.sum(self.hands[player.get_id()]) - 1
			stae[player_start+14] = self.bets[player.get_id()]
		dealer_start = 15 * len(self.players)
		state[dealer_start:dealer_start+13] = self.visible[self.dealer.get_id()]
		state[dealer_start+13] = np.sum(self.hands[self.dealer.get_id()]) - 1
		return state

	def get_profiles(self):
		profiles = np.zeros(6 * len(self.players))
		for i, player in enumerate(self.players):
			player_start = 6 * i
			profiles[player_start:player_start+6] = self.profiles[player.get_id()].get_stats()
		return profiles

	def get_profit(self, wins):
		profit = 0
		for i, player in enumerate(self.players):
			self.dealer_profit -= wins[i] * self.bets[player.get_id()]



	def print_game(self):
		print('Deck status')
		print(self.deck)
		for player in self.players:
			print('Player %s \'s cards' % player.get_id())
			print(self.hands[player.get_id()])
		print('Dealer\'s hand')
		print(self.hands[self.dealer.get_id()])

 