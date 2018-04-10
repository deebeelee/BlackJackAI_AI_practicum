import game
from dumbAI import dumbAI

dealer = dumbAI(200, 'd')
p1 = dumbAI(200, 'p1')
p2 = dumbAI(200, 'p2')
p3 = dumbAI(200, 'p3')
p4 = dumbAI(200, 'p4')
players = [p1, p2, p3, p4]
game = game.BlackjackGame(players, dealer)
print(game.check_wins())
game.print_game()
game.deal(p1)
game.print_game()
game.play_game()
game.print_game()
print(game.get_state())
print(game.get_profiles())
print(game.dealer_profit)