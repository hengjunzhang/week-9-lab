import random
import csv
import time
import os

class TicTacToe:
    def __init__(self, single_player=False):
        self.board = self.get_empty_board()
        self.current_player = 'X'
        self.single_player = single_player
        self.bot = 'O' if single_player else None
        self.start_time = None

        # Ensure log directory exists
        if not os.path.exists('logs'):
            os.makedirs('logs')

    def get_empty_board(self):
        return [[None, None, None] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print([cell if cell is not None else ' ' for cell in row])

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_input(self):
        if self.current_player == self.bot:
            empty_positions = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
            return random.choice(empty_positions)
        else:
            prompt = f"Player {self.current_player} > "
            player_input = input(prompt)
            row_col_list = player_input.split(',')
            return [int(x) for x in row_col_list]

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] is not None:
                return row[0]

        for i in range(3):
            column = [self.board[j][i] for j in range(3)]
            if len(set(column)) == 1 and column[0] is not None:
                return self.board[0][i]

        diag1 = [self.board[i][i] for i in range(3)]
        if len(set(diag1)) == 1 and diag1[0] is not None:
            return self.board[0][0]

        diag2 = [self.board[i][2-i] for i in range(3)]
        if len(set(diag2)) == 1 and diag2[0] is not None:
            return self.board[0][2]

        if all(cell is not None for row in self.board for cell in row):
            return "draw"

        return None

    def play_game(self):
        self.start_time = time.time()
        winner = None
        while winner is None:
            self.print_board()
            try:
                row, col = self.get_player_input()
                if self.board[row][col] is not None:
                    print("Spot taken, try again")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, try again.")
                continue

            self.board[row][col] = self.current_player
            winner = self.check_winner()
            self.switch_player()

        self.print_board()
        if winner == "draw":
            print("Draw")
        elif winner:
            print(f"Winner is {winner}")

        self.log_game_result(winner)

    def log_game_result(self, winner):
        end_time = time.time()
        game_duration = round(end_time - self.start_time, 2)
        log_data = {
            'Winner': winner,
            'Total Moves': sum(cell is not None for row in self.board for cell in row),
            'Start Time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start_time)),
            'End Time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)),
            'Game Duration': game_duration,
            'Game Mode': 'Single Player' if self.single_player else 'Two Player'
        }

        with open('logs/game_log.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=log_data.keys())
            if file.tell() == 0:  # Write header if file is empty
                writer.writeheader()
            writer.writerow(log_data)
