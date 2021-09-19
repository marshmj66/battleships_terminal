

def get_board():
    board = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],]
    return board

class Player1():
    def __init__(self,name):

        self.name = name
        self.hits = 0
        self.count = 0

    def placement(self):
        board = get_board()
        valid = False
        while valid == False:
            place = input('Please enter were you want to enter your two level ship: ').split()
            pos = input('what position you want it: (Right,Left,Up,or Down): ')
            place2 = input('Please enter were you want to enter your three level ship: ').split()
            pos2 = input('what position you want it: (Right,Left,Up,or Down): ')
            place3 = input('Please enter were you want to enter your four level ship: ').split()
            pos3 = input('what position you want it: (Right,Left,Up,or Down): ')

            angles = {
                'Right': int(place[1]) + 1,
                'Left': int(place[1]) + -1,
                'Down': int(place[0]) + 1,
                'Up': int(place[0]) + -1
            }
            angles2 = {
                'Right': int(place2[1]) + 3,
                'Left': int(place2[1]) + -2,
                'Down': int(place2[0]) + 3,
                'Up': int(place2[0]) + -2
            }
            angles3 = {
                'Right': int(place3[1]) + 4,
                'Left': int(place3[1]) + -3,
                'Down': int(place3[0]) + 4,
                'Up': int(place3[0]) + -3
            }


            if int(place[0]) >= 0 and int(place[1]) <= 4:
                board[int(place[0])][int(place[1])] = 1

            if pos == 'Right':
                if angles[pos] >= 0 and angles[pos] <= 4:
                    board[int(place[0])][angles[pos]] = 1
                    self.count += 1
            if pos2 == 'Right':
                if board[int(place2[0])][int(place2[1]):angles2[pos2]] == [0,0,0]:
                    board[int(place2[0])][int(place2[1]):angles2[pos2]] = [1,1,1]
                    self.count += 1
            if pos3 == 'Right':
                if board[int(place3[0])][int(place3[1]):angles3[pos3]] == [0,0,0,0]:
                    board[int(place3[0])][int(place3[1]):angles3[pos3]] = [1,1,1,1]
                    self.count += 1
            if pos == 'Left':
                if angles[pos] >= 0 and angles[pos] <= 4:
                    board[int(place[0])][angles[pos]] = 1
                    self.count += 1
            if pos2 == 'Left':
                if board[int(place2[0])][angles2[pos2]:int(place2[1])+1] == [0,0,0]:
                    board[int(place2[0])][angles2[pos2]:int(place2[1])+1] = [1,1,1]
                    self.count += 1
            if pos3 == 'Left':
                if board[int(place3[0])][angles3[pos3]:int(place3[1])+1] == [0,0,0,0]:
                    board[int(place3[0])][angles3[pos3]:int(place3[1])+1] = [1,1,1,1]
                    self.count += 1

            if pos == 'Down':
                if angles[pos] >= 0 and angles[pos] <= 4:
                    board[angles[pos]][int(place[1])] = 1
                    self.count += 1
            if pos2 == 'Down':
                for i in range(int(place2[0]),angles2[pos2]):
                    if board[i][int(place2[1])] == 0:
                        board[i][int(place2[1])] = 1
                        self.count += 1
            if pos3 == 'Down':
                for i in range(int(place3[0]),angles3[pos3]):
                    if board[i][int(place3[1])] == 0:
                        board[i][int(place3[1])] = 1
                        self.count += 1

            if pos == 'Up':
                if angles[pos] >= 0 and angles[pos] <= 4:
                    board[angles[pos]][int(place[1])] = 1
                    self.count += 1
            if pos2 == 'Up':
                for i in range(int(place2[0]), angles2[pos2] - 1, -1):
                    if board[i][int(place2[1])] == 0:
                        board[i][int(place2[1])] = 1
                        self.count += 1
            if pos3 == 'Up':
                for i in range(int(place3[0]), angles3[pos3] - 1, -1):
                    if board[i][int(place3[1])] == 0:
                        board[i][int(place3[1])] = 1
                        self.count += 1
            if self.count >= 3 or self.count == 8:
                print(self.count)
                print('ship placement valid')
                valid = True
            else:
                self.count = 0
                print('invalid placement try again')

        return board

    def attack(self,opponent):

        shot = input('> ')
        for l in shot:

            if l.isalpha():
                l = l.lower()
                x = ord(l)-97
                print(x)
            else:
                y = int(l)
        if x >= 0 and x <= 4 and y >= 0 and y <= 4:
            if opponent[x][y] == 1:
                opponent[x][y] = 'hit'
                self.hits += 1
            else:
                opponent[x][y] = 'miss'
        if self.hits == 2:
            return self.hits
        return opponent
class Player2(Player1):
    def __init__(self,name):
        super().__init__(name)


thing1 = Player1('Marshall')
board1 = thing1.placement()

thing2 = Player2('Charles')
board2 = thing2.placement()

for i in board1:
    print(i)
print('')
for i in board2:
    print(i)
def hid_board(board):
    hid = []
    symbol = {1:'blank',0:'blank','hit':'hit','miss':'miss'}
    letters = ['A','B','C','D','E']

    print('\t   1 \t  2 \t 3 \t    4 \t   5')
    print('__________________________________________')
    for row in range(len(board)):
        print(letters[row],end=' \t| ')
        for col in range(len(board[row])):
            value = symbol[board[row][col]]


            print(value,'|',end=' ')
        print('')
    print('_____________________________________________')




while True:
    show_board = []
    result = thing1.attack(board2)

    if result == 2 and thing1.hits == 2:
        print('player 1 wins by sinking the battleship')
        break

    for i in result:
        show_board.append(i)

    hid_board(show_board)

    show_board = []
    result = thing2.attack(board1)

    if result == 2 and thing2.hits == 2:
        print('player 2 sunked your battleship')
        break

    for i in result:
        show_board.append(i)

    hid_board(show_board)