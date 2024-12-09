def boardprint(board):
    print('-------------')
    for row in board:
        print('│' , ' │ '.join(row),'│')
        print('-------------')

def wincheck(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]  != ' ':
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return 0



boardlayout= '-------------\n│ 1 │ 2 │ 3 │\n-------------\n│ 4 │ 5 │ 6 │\n-------------\n│ 7 │ 8 │ 9 │\n-------------'

newboard= [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
count = 0 

print(boardlayout)
while count !=9:
    if count%2 == 0:
        turn = 'X'
    else:
        turn = 'O'

    choice= int(input(f'Player {turn}, enter a number of a box (1-9) : '))

    row = (choice -1)//3
    col=(choice -1)%3

    while newboard[row][col] != ' ':
        print('That space is not available')
        choice= int(input('Please enter the number a the box: '))
        row = (choice -1)//3
        col=(choice -1)%3

    newboard[row][col]= turn

    boardprint(newboard)
    
    winner= wincheck(newboard)
    if winner != 0:
        print(f"Player {winner} wins !!")
        count = 8

    count=count+ 1
if count ==9 and winner == 0:
    print("Its a tie ")


