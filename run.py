# 'O' indicates a miss
# 'X' indicates a hit

from random import randint

Hidden_Playfield = [[' '] * 7 for x in range(7)]
Guess_Playfield = [[' '] * 7 for x in range(7)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, }


def print_board(board):
    print('  A B C D E F G')
    print(' ***************')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1

#Enter the row number between 1 to 7

def get_ship_location():
    row = input('Please enter a valid row 1-7 ').upper()
    while row not in '1234567':
        print("Please enter a valid row ")
        row = input('Please enter a valid row 1-7 ')

#Enter the column from A TO G

    column = input('Please enter a valid column A-G ').upper()
    while column not in 'ABCDEFG':
        print("Please enter a valid column ")
        column = input('Please enter a valid column A-G ')
    return int(row) - 1, let_to_num[column]


#Function that creates the Battleship randomly

def create_ships(board):
    for ship in range(2):
        ship_r, ship_cl = randint(0, 6), randint(0, 6)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = randint(0, 6), randint(0, 6)
        board[ship_r][ship_cl] = 'X'


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
          if column == 'X':
            count += 1
    return count

#Print_board(Hidden_Playfield)

create_ships(Hidden_Playfield)
turns = 15
while turns > 0:
    print(' Welcome to Battleship!, Commander you have 15 tries to find the two Battleships')
    print_board(Guess_Playfield)
    row, column = get_ship_location()
    if Guess_Playfield[row][column] == 'O':
        print(' You already guessed that ')
    elif Hidden_Playfield[row][column] == 'X':
        print(' Congratulations!! You sunk the battleship ')
        Guess_Playfield[row][column] = 'X'
        turns -= 1
    else:
        print(' Sorry,You missed ')
        Guess_Playfield[row][column] = 'O'
        turns -= 1
    if count_hit_ships(Guess_Playfield) == 2:
        print(" Well Done!  ")
        break
    print(' You have ' + str(turns) + ' turns remaining ')
    if turns == 0:
        print(' Game Over, See you next time ')


