import time
import msvcrt
from grid import Grid

GRID_WIDTH = 120
GRID_HEIGHT = 40

game_grid = Grid(GRID_WIDTH, GRID_HEIGHT)


def score_write():
    filer = "log.txt"
    filew = "score.txt"

    with open(filer, 'r') as fr:
        dt = fr.readline()
        final = dt.split(',')
        data1 = "\n" + final[0] + ',' + final[1]+ ',' + final[2]
        #print(data1)
    with open(filew, 'a') as fw:
        fw.writelines(data1)

    fw.close()
    fr.close()


def game_loop(name1):
    x, y = game_grid.get_player_pos()
    game_grid.set_cell(x, y, 'C')

    while True:

        oldX, oldY = game_grid.get_player_pos()  # first get the old position

        '''
        Take player input from code as per it ASCAII value
        '''
        if msvcrt.kbhit():
            char = ord(msvcrt.getch())

            if char == 27:  # the ESC key code, exit game
                break
            elif char == 97:  # a key, move left
                x -= 1
            elif char == 100:  # d key, move right
                x += 1
            else:
                continue

        if not game_grid.check_Hbounds(x):
            x, y = oldX, oldY
        else:
            game_grid.set_cell(oldX, oldY, ' ')

        game_grid.set_player_pos(x, y)  # then set the new position
        game_grid.set_cell(x, y, 'C')

        # update the monsters
        game_grid.update()

        # draw the game board
        game_grid.draw(name1)


        time.sleep(0.1)  # 1/10 or 0.1

    score_write()
