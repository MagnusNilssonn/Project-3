# 'O' indicates a miss
# 'X' indicates a hit

from random import randint

Hidden_Playfield = [[' '] * 7 for x in range(7)]
Guess_Playfield = [[' '] * 7 for x in range(7)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6 }


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


def create_ships(board):
    pass


def count_hit_ships(board):
    pass



