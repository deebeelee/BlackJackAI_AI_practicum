import neat
import random
from game import BlackjackGame
from DBAI import DBAI
from dumbAI import dumbAI
from seventeenHits import seventeenHits
from fifteenHits import fifteenHits
from tabularAI import tabularAI
from smart_dealer import SmartDealer

def select_player():
	choice = random.randint(0,4)
	initial_money = 200
	if choice == 0:
		return fifteenHits(initial_money, 'fifteen')
	elif choice == 1:
		return DBAI(initial_money, 'DB')
	elif choice == 2:
		return seventeenHits(initial_money, 'seventeen')
	elif choice == 3:
		return dumbAI(initial_money, 'dumb')
	else:
		return tabularAI(initial_money, 'tabular')

def eval_genomes(genomes, config):
	player_list = []
	for i in range(4):
		player_list.append(select_player())
	for genome_id, genome in genomes:
		net = neat.nn.FeedForwardNetwork.create(genome, config)
		dealer = SmartDealer(net, 'Smart')
		game = BlackjackGame(player_list, dealer)
		game.play_games(1000)
		genome.fitness = game.dealer_profit

def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    

    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    #p.run(eval_genomes, 10)
    
    return winner_net
