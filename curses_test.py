import curses

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import _curses

fella = (
    ' o ',
    '/|\\',
    '/ \\'
)


def draw_menu(stdscr: '_curses.window'):
    begin_x = 10
    begin_y = 10
    height = 1
    width = 20

    test_win = curses.newwin(height, width, begin_y, begin_x)
    test_win.addstr("hello, world", curses.A_REVERSE)
    test_win.refresh()

    stdscr.refresh()
    stdscr.getch()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
