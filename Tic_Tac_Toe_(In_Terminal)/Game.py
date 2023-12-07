def check_winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=' ': 
            return True
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=' ': 
            return True
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=' ': 
        return True
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=' ': 
        return True
    return False

def tic_tac_toe():
    board=[[' ']*3 for _ in range(3)]
    player='X'

    for _ in range(9):
        print("\n".join(map(str, board)))
        print(f"Player {player}, make your move")
        row=int(input("Enter the row: ")) 
        col=int(input("Enter the column: ")) 

        if board[row][col]!=' ':
            print("\nInvalid move, please try again\n")
            continue

        board[row][col]=player

        if check_winner(board):
            print("\n".join(map(str, board)))
            print(f'\nCongratulations, Player {player} wins!!!\n')
            return

        player='O' if player=='X' else 'X'

    print("It's a draw!")

tic_tac_toe()