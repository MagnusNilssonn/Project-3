# 'O' indicates a miss
# 'X' indicates a hit

Hidden_Playfield = [[' '] * 7 for x in range(7)]
Guess_Playfield = [[' '] * 7 for x in range(7)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6 }

def print_board(board):
    print('  A B C D E F G')
    print(' ****************')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row )))
        row_num += 1
        


def get_ship_location():
    pass


def create_ships(board):
    pass


def count_hit_ships(board):
    pass



