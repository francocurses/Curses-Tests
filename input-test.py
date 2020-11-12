import curses
import random

def main(stdscr):
    # initial screen
    curses.curs_set(False)
    stdscr.addstr(0, 0, "#####################")
    stdscr.addstr(1, 0, "# type something:")
    stdscr.addstr(2, 0, "#####################")

    # program loop
    while True:
        # select random color pair
        cc = colors.copy()
        cf = cc.pop(random.randrange(len(cc)))
        cb = cc.pop(random.randrange(len(cc)))
        curses.init_pair(1, cf, cb)
        cp = curses.color_pair(1)
        
        # select random attribute
        ac = attributes.copy()
        attr = random.choice(ac)

        # get user keypress
        k = stdscr.getkey()

        # print in screen
        stdscr.addstr(1, 18, " "*(curses.COLS-18))
        stdscr.addstr(1, 18, k, cp+attr)

colors = [curses.COLOR_BLACK,
          curses.COLOR_BLUE,
          curses.COLOR_CYAN,
          curses.COLOR_GREEN,
          curses.COLOR_MAGENTA,
          curses.COLOR_RED,
          curses.COLOR_WHITE,
          curses.COLOR_YELLOW]

attributes = [curses.A_NORMAL,
              curses.A_BOLD,
              curses.A_DIM,
              curses.A_UNDERLINE,
              curses.A_ITALIC]

curses.wrapper(main)
