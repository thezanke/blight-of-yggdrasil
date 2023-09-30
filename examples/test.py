import curses

def main(stdscr):
    # Initialize the screen
    curses.curs_set(0)
    stdscr.clear()

    def redraw(h, w):
        container_h, container_w = h, (w - 10) // 10
        container_y, container_x = 0, 0
        containers = []
        for i in range(10):
            container = curses.newwin(container_h, container_w, container_y, container_x)
            container.border()
            containers.append(container)
            container_x += container_w + 1

        stdscr.refresh()
        for container in containers:
            container.refresh()

    # Initial draw
    h, w = stdscr.getmaxyx()
    redraw(h, w)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_RESIZE:
            h, w = stdscr.getmaxyx()
            stdscr.clear()
            redraw(h, w)

if __name__ == "__main__":
    curses.wrapper(main)
