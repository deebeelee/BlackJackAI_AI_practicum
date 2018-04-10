import game
from dumbAI import dumbAI
from fifteenHit import fifteenHits
from seventeenHit import seventeenHits


dealer = dumbAI(200, 'd')
p1 = fifteenHits(200, 'p1')
p2 = seventeenHits(200, 'p2')
p3 = DBAI(200, 'p3')
p4 = dumbAI(200, 'p4')
players = [p1, p2, p3, p4]
game = game.BlackjackGame(players, dealer)
game.print_game()
game.play_game()
game.print_game()
print(game.get_state())
print(game.get_profiles())
print(game.dealer_profit)
print(game.check_wins())

