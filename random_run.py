import random
from tqdm import tqdm

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        if current_player == 'X':
            row, col = random.randint(0, 2), random.randint(0, 2)
            while board[row][col] != ' ':
                row, col = random.randint(0, 2), random.randint(0, 2)
        else:
            row, col = random.randint(0, 2), random.randint(0, 2)
            while board[row][col] != ' ':
                row, col = random.randint(0, 2), random.randint(0, 2)

        board[row][col] = current_player

        if check_winner(board, current_player):
            return current_player

        if is_board_full(board):
            return 'TIE'

        current_player = 'O' if current_player == 'X' else 'X'

def simulate_games(num_games):
    results = {'X': 0, 'O': 0, 'TIE': 0}
    
    for _ in tqdm(range(num_games), desc="Simulating Games", unit="game"):
        outcome = play_tic_tac_toe()
        results[outcome] += 1

    return results

if __name__ == "__main__":
    num_simulations = 1000
    simulation_results = simulate_games(num_simulations)

    print(f"\nSimulation results for {num_simulations} games:")
    print(f"The player who goes first wins: {simulation_results['X']} times ({(simulation_results['X'] / num_simulations) * 100:.2f}%)")
    print(f"The player who goes second wins: {simulation_results['O']} times ({(simulation_results['O'] / num_simulations) * 100:.2f}%)")
    print(f"Ties: {simulation_results['TIE']} times ({(simulation_results['TIE'] / num_simulations) * 100:.2f}%)")
