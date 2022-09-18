import os
from random import randint

'''
This is a code to create a class which will have method to initialize the game board.
It will have methods to update the game states and to update the scores.
'''


class Grid:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.grid = self.create()
        self.p_x = self.WIDTH // 2
        self.p_y = self.HEIGHT - 2
        self.set_player_pos(self.p_x, self.p_y)
        self.timer = 2
        self.catched = 0
        self.lost = 0



    def create(self):
        brd = []
        for h in range(self.HEIGHT):
            brd.append([])
            for w in range(self.WIDTH):
                if w < 1 or w == self.WIDTH - 1:
                    brd[h].append('x')
                elif h == self.HEIGHT - 1:
                    brd[h].append('x')
                else:
                    brd[h].append(' ')
        return brd

    '''
    Save game data to a file after each game over.
    '''

    def save_game(self, catch, lost, player_name):
        # fields = ['Catched Bugs']
        filename = "log.txt"
        # writing to csv file
        with open(filename, 'w') as wr:
            # creating a csv writer object
            data_score = player_name + ',' + str(catch) + ',' + str(lost)
            wr.write(data_score)

    '''
    It will draw the board as game continue.
    '''


    def draw(self, p_name):
        self.clear()
        for row in self.grid:
            for character in row:
                print(character, end='')
            print()

        print("Monsters Catched: " + str(self.catched) + "    " + "Monsters escaped: " + str(self.lost))
        print("wow!", p_name, 'Your are doing great. Keep On Playing the Game\n')
        print("You can definitely score a lot. You should notice time while  playing.\n")
        print("You can exit the game any time by pressing 'ESC' button on keyboard.\n")
        self.save_game(self.catched, self.lost, p_name)

    '''
    This method will update game state.
    '''

    def update(self):
        self.timer -= 0.5
        if self.timer < 0:
            self.add_mons(randint(1, self.WIDTH - 2), 1)
            self.timer = randint(1, 5)

        self.move_mons()

    def clear(self):
        os.system('cls')  # only works with CMD and Powershell, doesn't work with Git-Bash

    def set_player_pos(self, x, y):
        self.p_x, self.p_y = x, y

    def get_player_pos(self):
        return self.p_x, self.p_y

    def set_cell(self, x, y, chr):
        self.grid[y][x] = chr

    def get_cell(self, x, y):
        return self.grid[y][x]

    # Horizonal bound
    def check_Hbounds(self, x):
        return x > 0 and x < self.WIDTH - 1

    ##Vertical bounds bound
    def check_Vbounds(self, y):
        return y >= 0 and y < self.HEIGHT - 2

    def add_mons(self, x, y):
        self.grid[y][x] = 'M'

    '''
    This method will move the monsters and populate them to game board.
    '''

    def move_mons(self):
        for y in range(len(self.grid) - 1, 0, -1):
            for x in range(len(self.grid[y])):
                if self.get_cell(x, y) == 'M' and self.check_Vbounds(y):
                    self.set_cell(x, y, ' ')
                    self.set_cell(x, y + 1, 'M')
                    if self.get_cell(x, y + 2) == 'C':
                        self.catched += 1
                elif self.get_cell(x, y) == 'M':
                    self.set_cell(x, y, ' ')
                    self.lost += 1
