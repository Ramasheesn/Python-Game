import time
import pyfiglet
from rich import print
import msvcrt as m
from game import game_loop

'''
This is displayed when the game will load and will provide a menu list.
'''


def game_board():
    title = pyfiglet.figlet_format('GAME ZONE', font='isometric2')
    print(f'[yellow]{title}[/yellow]')
    time.sleep(1)
    print("Enter number to select from below menu.\n\n")
    print(
        "(0) Play Game.            (1) score card.\n\n(2) Game help.            (3) Exit from main Menu.\n")


# game_board()

'''
This will craete player profile.
'''


def create_user():
    print("Enter your name.\n")
    name = input()
    print("Hi! ", name, "let play game.\n")
    return name


'''
This will write current catched mosnters as score to a file called 'Score.csv'
'''


def exe():
    if m.kbhit():
        char = ord(m.getch())
        if char == 27:
            exit()


def score_card(name):
    filename = "score.txt"
    flag = 0
    with open(filename, 'r') as cf:
        for ln in cf:
            lst = ln.split(',')
            if lst[0].lower() == name.lower():
                count = int(lst[1]) + int(lst[2])
                print(lst[0], "destroyed total", lst[1], "Out of total", count, "Monsters")
                flag = 1
                break
            else:
                continue
        if flag == 0:
            print("Payer,", name, "not found.")


def lost_old(lost_mons):
    return lost_mons


def catch_old(catch_mons):
    return catch_mons


def wait():
    m.getch()


'''
Code to print player score.
'''


def player_name():
    print("Enter player name.\n")
    name = input()
    return name


def helper():
    print("To play the Game we need to following below instructions.\n" +
          "1.Press 'ESC' to exit the Game anytime.\n " +
          "2. Press 'a' key to  move left\n " +
          "3. Press 'd' key to move right ")
    starter()


def starter():
    game_board()
    option = input()
    if option == '0':
        name = create_user()
        input("Press Enter to Continue")
        game_loop(name)
    elif option == '1':
        score_card(player_name())
        starter()

    elif option == '2':
        helper()
    elif option == '3':
        exe()
    else:
        print("Enter number from 0 to 9 correct option")
        starter()


starter()
