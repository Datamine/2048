# John Loeber | Python 2.7.8 | 15-Nov-2014 | www.johnloeber.com

from copy import deepcopy
from random import randint
import locale
import sys
import os
import curses

# path to file where we store the max score
STORE_FILE_PATH = "~/.2048.txt"

def get_max_score():
    """
    retrieve max score from the store-file
    """
    if os.path.isfile(STORE_FILE_PATH):
        with open(STORE_FILE_PATH, "r") as f:
            return f.readlines()[1].rstrip('\n')
    else:
        return "0"

def write_max_score(score):
    """
    write max score to the store-file
    """
    with open(STORE_FILE_PATH, "w+") as f:
        first_line = f.readline()
        return f.write(first_line + str(score))

class Board():
    """
    represents a 2048 game board
    """

    KEY_OPTS = {
        curses.KEY_DOWN:  "down",
        curses.KEY_RIGHT: "right",
        curses.KEY_LEFT:  "left",
        curses.KEY_UP:    "up",
        ord('Q'):         "quit",
        ord('q'):         "quit",
        ord('h'):         "left",
        ord('H'):         "left",
        ord('j'):         "down",
        ord('J'):         "down",
        ord('k'):         "up",
        ord('K'):         "up",
        ord('l'):         "right",
        ord('L'):         "right"
    }

    def __init__(self):
        self.board = self.make_blank_board()
        self.win = False
        self.new_coord = []
        self.max_score = get_max_score()
        self.score = 0
        return

    def make_blank_board(self):
        """
        creates a game board with all slots blank
        """
        return []

    def get_score(self):
        """
        computes the score on the board, returns it as a string.
        """
        return str(sum(int(x) for x in [y for y in self.board if y != '']))

    def display(self):
        """
        prints the current board to the screen.
        there are marginally more efficient ways we could do this: e.g. not
        clear the entire screen but rather just refresh certain characters.
        """
        global stdscr
        stdscr.erase()
        stdscr.addstr(2, 5, "Documentation is at www.johnloeber.com/docs/2048.html."
                            "\n     Press 'q' to quit.")

        # create the strings to represent the current items on the board
        max_len = max(len(i) for i in self.board)
        board_copy = deepcopy(self.board)
        for index, board_item in enumerate(board_copy):
            board_copy[index] = "[" + (" " * (max_len - len(board_item))) + board_item + "] "

        # print those strings to the screen
        board_indices = [[0, 1, 2, 3],
                         [4, 5, 6, 7],
                         [8, 9, 10, 11],
                         [12, 13, 14, 15]]
        for index, row in enumerate(board_indices):
            to_write = ""
            for cell_index in row:
                to_write += board_copy[cell_index]
            stdscr.addstr(index+5, 5, to_write)

        # writes the new coordinates in bold, over the current board.
        for i in self.new_coord:
            row = i / 4
            entry = (i % 4) * len(board_copy[i])
            stdscr.addstr(row+5, entry+5, board_copy[i], curses.A_BOLD)

        # if the user has won, write a congratulatory message
        if self.win:
            win_message = "Congratulations, you win! Keep playing if you wish."
            stdscr.addstr(10, 5, win_message)

        # write the current and max scores
        stdscr.addstr(3, 46 - len(self.max_score), "Best Score: " + self.max_score)
        stdscr.addstr(4, 43 - len(self.score), "Current Score: " + self.score)

        stdscr.refresh()
        return

    def spawn(self):
        """
        spawn a new integer on the board.
        """
        if '' in self.board:
            empty_indices = [index for index, cell in enumerate(self.board) if cell == '']
            random_loc = randint(0, len(empty_indices)-1)
            # one-in-ten chance of getting a '4' instead of a '2'
            chance = randint(1, 10)
            if chance == 10:
                self.board[empty_indices[random_loc]] = '4'
            else:
                self.board[empty_indices[random_loc]] = '2'
            self.new_coord = empty_indices[random_loc]
        return

    def update_score(self):
        """
        retrieve the current score, compare it to the max score, update if necessary.
        """
        self.score = self.get_score()
        if int(self.score) > int(self.max_score):
            write_max_score(self.score)
            self.max_score = self.score
        return

    def get_move(self):
        """
        get the player's next move.
        if the move is invalid, flash an error to the game screen.
        """
        global stdscr
        char = stdscr.getch()

        if char in self.KEY_OPTS:
            return self.KEY_OPTS[char]
        else:
            stdscr.addstr(11, 5, "Not an arrow key! Try again.")
            stdscr.refresh()
            self.get_move()
        return

    def check(self):
        """
        check if the user has lost.
        handle the case if the user has lost.
        """

        # if a square is empty, the game's still going on.
        if '' in self.board:
            return

        possible_moves = ["up", "down", "left", "right"]
        next_possible_game_states = [newboard(self.board, move) for move in possible_moves]
        # if all next possible game states are the same as the current, then game over.
        if all(game_state == self.board for game_state in next_possible_game_states):
            global stdscr
            stdscr.move(10,0)
            stdscr.clrtoeol()
            stdscr.addstr(10,5,"Game Over! Press 't' to try again.")
            stdscr.refresh()
            while True:
                c = stdscr.getch()
                if c not in [ord('q'),ord('Q'),ord('t'),ord('T')]:
                    continue
                else:
                    # this syntactic choice to avoid memory leaks (nested games)
                    break
            if c==ord('q') or c==ord('Q'):
                stop()
            elif c==ord('t') or c==ord('T'):
                game()




# reset newcoords for next iteration in game loop
newcoord = []

def strip(items):
    """
    newboard helper:
    filters a list, returns the items that aren't the empty string, in order.
    """
    return [item for item in items if item != '']

def weave(list1, list2, list3, list4):
    """
    newboard helper:
    no idea.
    """
    x = []
    for i in range(0, 4):
        for j in [list1, list2, list3, list4]:
            x.append(j[i])
    return x

# helper for newboard
def fill(l):
    if len(l)<4:
        l += ['']*(4-len(l))
    return l

# This is particularly ugly. I wrote it some months ago. It seems inelegant,
# but folding the list correctly is actually a remarkably difficult task
# given the number of edge cases and particularities. Consequently, I wrote
# this bruteforce function to just get the job done -- writing a nice, higher-
# level reduce-type function to do this proved difficult. I think the ugliness
# of this function stems from my choice of data structure (flat list) for the
# board, which was probably a mistake. A class-based structure would allow
# for a more elegant solution and handling of new moves.
def newboard(board,move):
    # process a move, and return the consequent state of the board.
    if move=="quit":
        stop()
    elif move=="up" or move=="down":
        parts = [[board[0],board[4],board[8],board[12]],
                 [board[1],board[5],board[9],board[13]],
                 [board[2],board[6],board[10],board[14]],
                 [board[3],board[7],board[11],board[15]]]
    else:
        parts = [board[0:4],
                 board[4:8],
                 board[8:12],
                 board[12:16]]
    # i'll be "folding" the sublists, so i'm now arranging them to have them
    # cascade properly.
    if move=="down" or move=="right":
        for x in range(len(parts)):
            parts[x] = parts[x][::-1]
            # all folds will go left (or up), hence the need to reverse lists
    newparts = [[],[],[],[]]
    # and here the cascading fold begins.
    for i in range(4):
        newl = strip(parts[i])
        if len(newl)==0:
            continue
        elif len(newl)==1:
            newparts[i].append(newl[0])
        elif len(newl)==2:
            if newl[0]==newl[1]:
                newparts[i].append(str(int(newl[0])+int(newl[1])))
            else:
                newparts[i].append(newl[0])
                newparts[i].append(newl[1])
        elif len(newl)==3:
            if newl[0]==newl[1]:
                newparts[i].append(str(int(newl[0])+int(newl[1])))
                newparts[i].append(newl[2])
            else:
                newparts[i].append(newl[0])
                if newl[1]==newl[2]:
                    newparts[i].append(str(int(newl[1])+int(newl[2])))
                else:
                    newparts[i].append(newl[1])
                    newparts[i].append(newl[2])
        else:
            if newl[0]==newl[1]:
                newparts[i].append(str(int(newl[0])+int(newl[1])))
                if newl[2]==newl[3]:
                    newparts[i].append(str(int(newl[2])+int(newl[3])))
                else:
                    newparts[i].append(newl[2])
                    newparts[i].append(newl[3])
            else:
                newparts[i].append(newl[0])
                if newl[1]==newl[2]:
                    newparts[i].append(str(int(newl[1])+int(newl[2])))
                    newparts[i].append(newl[3])
                else:
                    newparts[i].append(newl[1])
                    if newl[2]==newl[3]:
                        newparts[i].append(str(int(newl[2])+int(newl[3])))
                    else:
                        newparts[i].append(newl[2])
                        newparts[i].append(newl[3])
    for x in range(4):
        newparts[x] = fill(newparts[x])
    if move=="up":
        return weave(newparts[0],newparts[1],newparts[2],newparts[3])
    elif move=="down":
        return weave(newparts[0][::-1],newparts[1][::-1],newparts[2][::-1],newparts[3][::-1])
    elif move=="right":
        return newparts[0][::-1] + newparts[1][::-1] + newparts[2][::-1] + newparts[3][::-1]
    else:
        return [x for sublist in newparts for x in sublist]

# end the application
def stop():
    # undo all curses-stuff
    global stdscr
    stdscr.keypad(0)
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()
    sys.exit(0)
    return

def game():
    # initialize a new game
    global newcoord,stdscr,win,maxscore
    newcoord = []
    win = False
    board = spawn(spawn(['']*16))
    printboard(board)
    # game loop
    while True:
        check(board)
        board2 = board
        # so user submits keypresses that change the state of the game
        while(board2==board):
            move = getmove()
            board2 = newboard(board,move)
        # once state has changed, spawn new int
        board2 = spawn(board2)
        if "2048" in board2:
            win = True
        printboard(board2)
        board = board2

def main(screen):
    locale.setlocale(locale.LC_ALL, '')
    global stdscr
    stdscr=curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)
    curses.curs_set(0)
    game()

if __name__ == '__main__':
    curses.wrapper(main)
