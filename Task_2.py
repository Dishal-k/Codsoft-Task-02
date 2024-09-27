import math

# Initialize the game board
board = [' ' for _ in range(9)]


def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']


def is_board_full(board):
    return ' ' not in board


def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions


def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score


def best_move(board):
    best_score = -math.inf
    move = None
    for i in available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move


def play_game():
    print_board(board)
    while True:
        # Human player's turn
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[human_move] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI player's turn
        print("AI is making a move...")
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break


# Run the game
play_game()