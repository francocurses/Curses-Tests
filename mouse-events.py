import curses
import random

def main(stdscr):
    # curses configuration
    curses.curs_set(False)
    curses.mousemask(2**32-1)

    # initial screen
    text =  "Catching mouse events: "
    clearstr = " "*(curses.COLS-len(text))
    stdscr.addstr(0, 0, text)

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

        # get key
        k = stdscr.getkey()

        if k=="KEY_MOUSE":
            i, x, y, z, bstate = curses.getmouse()
            stdscr.addstr(0, len(text), clearstr)
            stdscr.move(0, len(text))
            stdscr.addstr(k+",")
            stdscr.addstr(str(i)+",")
            stdscr.addstr(str(x)+",")
            stdscr.addstr(str(y)+",")
            stdscr.addstr(str(z)+",")
            stdscr.addstr(str(bstate), attr | cp)

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
