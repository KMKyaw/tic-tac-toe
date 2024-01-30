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

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        move_val = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '

        if move_val > best_val:
            best_move = move
            best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        if current_player == 'X':
            row, col = best_move(board)
        else:
            row, col = best_move(board)

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
    num_simulations = 100
    simulation_results = simulate_games(num_simulations)

    print(f"\nSimulation results for {num_simulations} games:")
    print(f"Player X wins: {simulation_results['X']} times ({(simulation_results['X'] / num_simulations) * 100:.2f}%)")
    print(f"Player O wins: {simulation_results['O']} times ({(simulation_results['O'] / num_simulations) * 100:.2f}%)")
    print(f"Ties: {simulation_results['TIE']} times ({(simulation_results['TIE'] / num_simulations) * 100:.2f}%)")
