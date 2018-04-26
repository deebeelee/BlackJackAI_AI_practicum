import os
import game as gg
from dumbAI import dumbAI
from fourteenHits import fourteenHits
from fifteenHits import fifteenHits
from sixteenHits import sixteenHits
from seventeenHits import seventeenHits
from Dealer import Dealer
from DBAI import DBAI
from tabularAI import tabularAI
from smart_dealer import SmartDealer
import neatTrain

configuration_file = os.path.join( os.path.dirname(__file__), 'config-feedforward')

neural_net = neatTrain.run(configuration_file)

print("We are done training the neural network.")

dealer = SmartDealer(neural_net,'dealer')
p1 = fourteenHits(200,'p1')
p2 = fifteenHits(200,'p2')
p3 = sixteenHits(200,'p3')
p4 = seventeenHits(200,'p4')
players = [p1, p2, p3, p4]
total_wins = [0,0,0,0]
total_losses = [0,0,0,0]
total_draws = [0,0,0,0]
total_win_loss_ratio = [0.0,0.0,0.0,0.0]
for i in range(10000):
    game = gg.BlackjackGame(players, dealer)
    #game.print_game()
    game.play_game()
    #game.print_game()
    #print(game.get_state())
    #print(len(game.get_state()))
    #print(game.get_profiles())
    #print(game.dealer_profit)
    game_stats = game.check_wins()
    for i in range(4):
        if(game_stats[i] == 1):
            total_wins[i] += 1
        elif(game_stats[i] == -1):
            total_losses[i] += 1
        else:
            total_draws[i] += 1
    #print(game.check_wins())

print("Game statistics")

for i in range(4):
    total_win_loss_ratio[i] = (total_wins[i])/(total_losses[i])
print(total_wins)
print(total_draws)
print(total_losses)
print(total_win_loss_ratio)

