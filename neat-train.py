import neat
import random
from game import BlackjackGame
from DBAI import DBAI
from dumbAI import dumbAI
from seventeenHit import seventeenHit
from fifteenHit import fifteenHit
from tabularAI import tabularAI
from smart_dealer import SmartDealer

def select_player():
	choice = random.randint(0,4)
	initial_money = 200
	if choice == 0:
		return fifteenHit(initial_money, 'fifteen')
	elif choice == 1:
		return DBAI(initial_money, 'DB')
	elif choice == 2:
		return seventeenHit(initial_money, 'seventeen')
	elif choice == 3:
		return dumbAI(initial_money, 'dumb')
	else:
		return tabularAI(initial_money, 'tabular')

def eval_genomes(genomes, config):
	player_list = []
	for i in range(4):
		player_list.append(select_player())
	for genome_id, genome in genomes:
		genome.fitness = 4.0
		net = neat.nn.FeedForwardNetwork.create(genome, config)
		game = BlackjackGame(player_list, dealer)
		game.play_games(1000)
		genome.fitness = game.dealer_profit
