import game as gg
from dumbAI import dumbAI
from fifteenHit import fifteenHits
from seventeenHit import seventeenHits
from Dealer import Dealer
from DBAI import DBAI
from tabularAI import tabularAI

dealer = dumbAI(200,'dealer')
p1 = DBAI(200,'p1')
p2 = fifteenHits(200,'p2')
p3 = seventeenHits(200,'p3')
p4 = tabularAI(200,'p4')
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

