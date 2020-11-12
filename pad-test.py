import curses

def main(stdscr):
    # curses configuration
    curses.curs_set(False)

    # define pad
    s = ". scroll with arrows"
    pad = curses.newpad(10, 22)
    for i in range(10):
        pad.addstr(i, 0, str(i)+s)
    padpos = 0
    stdscr.refresh()
    pad.refresh(padpos, 0, 0, 0, 0, 20)

    while(True):
        k = stdscr.getkey()
        if k=="KEY_DOWN" and padpos<9:
            padpos += 1
        elif k=="KEY_UP" and padpos>0:
            padpos -= 1
        pad.refresh(padpos, 0, 0, 0, 0, 20)

curses.wrapper(main)
