import curses
import random

def main(stdscr):
    # curses configuration
    curses.curs_set(False)
    curses.echo()

    # initial screen
    stdscr.addstr(0, 0, "Type something: ")
    stdscr.addstr(1, 0, "My response is: ")

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

        # get user string
        stdscr.move(0, 16)
        k = stdscr.getkey()
        stdscr.addstr(0, 16, " "*(curses.COLS-16))
        stdscr.addstr(0, 16, k)
        s = stdscr.getstr()
        s = k+s.decode()

        # print in screen
        stdscr.addstr(1, 16, " "*(curses.COLS-16))
        stdscr.addstr(1, 16, s, cp+attr)

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
