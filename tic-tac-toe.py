# Jogo do Galo (Tic Tac Toe)


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for turn in range(9):
        print_board(board)
        row = int(input(f"Jogador {current_player}, escolha a linha (0-2): "))
        col = int(input(f"Jogador {current_player}, escolha a coluna (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Jogador {current_player} venceu!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Casa já ocupada! Tente novamente.")
            
    print_board(board)
    print("Empate!")


if __name__ == "__main__":
    tic_tac_toe()
