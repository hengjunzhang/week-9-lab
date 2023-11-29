from tictactoe import TicTacToe
import csv
import datetime

def log_game_result(winner, game_mode):
    with open('logs/game_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        now = datetime.datetime.now()
        writer.writerow([now, game_mode, winner])

if __name__ == '__main__':
    single_player = input("Single player mode? (y/n): ").lower() == 'y'
    game_mode = 'Single' if single_player else 'Multi'
    game = TicTacToe(single_player)
    winner = game.play_game()
    log_game_result(winner, game_mode)
