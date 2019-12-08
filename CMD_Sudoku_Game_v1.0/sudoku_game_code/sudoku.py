import curses
import time
from pygame import mixer

menu = ["New Game", "Exit"]

exit_text = ["Are you sure want to quit?", "YES", "NO"]

sudoku_blocks = [
    [9, ".", ".", ".", ".", ".", ".", ".", 1],
    [".", ".", ".", 7, ".", ".", ".", ".", 2],
    [8, 6, 5, ".", 3, ".", 7, ".", "."],

    [2, ".", ".", 6, ".", 4, ".", 7, "."],
    [".", 1, ".", ".", ".", ".", ".", 2, "."],
    [".", 4, ".", 8, ".", 1, ".", ".", 9],

    [".", ".", 8, ".", 1, ".", 9, 3, 5],
    [4, ".", ".", ".", ".", 5, ".", ".", "."],
    [6, ".", ".", ".", ".", ".", ".", ".", 7]
]


def is_sudoku_correct(screen,sudoku_blocks):
    def is_all_input_correct(sudoku_blocks):
        for i in sudoku_blocks:
            for a in range(0,9):
                if isinstance(i[a], int):
                    pass
                elif i[a].isdigit():
                    continue
                else:
                    print_center(screen,"Please fill in all places.")
                    time.sleep(3)
                    sudoku(screen,sudoku_blocks)
                    return False
        return True

    def is_vertical_correct(sudoku_blocks):
        for b in range(0,9):
            control_list = []
            for i in sudoku_blocks:
                control_list.append(int(i[b]))
            control_list.sort()
            control_number = 1
            for a in control_list:
                if a == control_number:
                    control_number += 1
                else:
                    return False
        return True


    def is_horizontal_correct(sudoku_blocks):
        for b in range(0,9):
            control_list = []
            for a in sudoku_blocks[b]:
                control_list.append(int(a))
            control_list.sort()
            control_number = 1
            for a in control_list:
                if a == control_number:
                    control_number += 1
                else:
                    return False
        return True

    def is_block_correct(sudoku_blocks):
        for d in range(0, 7, 3):
            for a in range(0, 7, 3):
                control_list = []
                for b in range(0, 3):
                    for c in range(0, 3):
                        control_list.append(int(sudoku_blocks[b + d][c + a]))
                control_list.sort()
                control_number = 1
                for a in control_list:
                    if a == control_number:
                        control_number += 1
                    else:
                        return False
        return True

    if is_all_input_correct(sudoku_blocks):
        if is_horizontal_correct(sudoku_blocks) and is_vertical_correct(sudoku_blocks) and is_block_correct(sudoku_blocks):
            return True
        else:
            print_center(screen,"You LOST!")
            return False
    return False



def change_number(current_number_id, key, sudoku_blocks):
    if isinstance(sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1], str):
        if key == 48:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "."

        if key == 49:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "1"

        if key == 50:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "2"

        if key == 51:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "3"

        if key == 52:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "4"

        if key == 53:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "5"

        if key == 54:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "6"

        if key == 55:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "7"

        if key == 56:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "8"

        if key == 57:
            sudoku_blocks[(current_number_id-1) // 9][current_number_id % 9 - 1] = "9"


def draw_frame(screen):
    for a in range(0, 13, 4):
        screen.hline(a, 0, curses.ACS_HLINE, 25)
    for a in range(0, 25, 8):
        screen.vline(0, a, curses.ACS_VLINE, 12)
    for a in range(0, 13, 4):
        for b in range(0, 25, 8):
            screen.addch(a, b, curses.ACS_PLUS)


def draw_sudoku(screen, sudoku_blocks, current_number_id):
    for b in range(1, 10):
        for a in range(2, 20, 2):
            if current_number_id == ((b - 1) * 9 + (a // 2)):
                screen.attron(curses.color_pair(1))
                screen.addstr(int(b + (b // 3.5)), (a // 7) * 2 + a, str(sudoku_blocks[b - 1][a // 2 - 1]))
                screen.attroff(curses.color_pair(1))
            else:
                if isinstance(sudoku_blocks[b - 1][a // 2 - 1], str):
                    screen.addstr(int(b + (b // 3.5)), (a // 7) * 2 + a, str(sudoku_blocks[b - 1][a // 2 - 1]),
                                  curses.A_UNDERLINE)
                else:
                    screen.addstr(int(b + (b // 3.5)), (a // 7) * 2 + a, str(sudoku_blocks[b - 1][a // 2 - 1]))


def sudoku(screen, sudoku_blocks):
    screen.clear()
    curses.curs_set(0)
    draw_frame(screen)
    current_number_id = 1
    draw_sudoku(screen, sudoku_blocks, current_number_id)

    while True:
        key = screen.getch()

        if key == curses.KEY_RESIZE:
            screen.clear()
            curses.resize_term(0, 0)

        if key == curses.KEY_RIGHT and current_number_id < 81:
            current_number_id += 1
        if key == curses.KEY_LEFT and current_number_id > 1:
            current_number_id -= 1
        if key == curses.KEY_UP and 0 < (current_number_id // 9) and 0 < current_number_id < 82:
            current_number_id -= 9
        if key == curses.KEY_DOWN and (current_number_id // 9) < 8 and 0 < current_number_id < 82:
            current_number_id += 9

        if 48 <= key <= 57:
            change_number(current_number_id, key, sudoku_blocks)

        if key == curses.KEY_ENTER or key in [10, 13] :
            if is_sudoku_correct(screen,sudoku_blocks):
                print_center(screen,"You WIN!")
                time.sleep(3)
                main_menu(screen,0)
                break
            else:
                time.sleep(3)
                main_menu(screen,0)
                break

        if key == 27:
            exit_screen(screen)

        draw_frame(screen)
        draw_sudoku(screen, sudoku_blocks, current_number_id)
        screen.refresh()


def exit_menu(screen, selected_row_idx):
    screen.clear()
    h, w = screen.getmaxyx()

    x = w // 2 - len(exit_text[0]) // 2
    y = h // 2 - len(exit_text) // 2 - 1
    screen.addstr(y, x, exit_text[0])

    x = w // 2 - len(exit_text[1]) // 2
    y = h // 2 - len(exit_text) // 2 + 1

    if selected_row_idx == 0:
        screen.attron(curses.color_pair(1))
        screen.addstr(y, x - 5, exit_text[1])
        screen.attroff(curses.color_pair(1))
        screen.addstr(y, x + 5, exit_text[2])
    if selected_row_idx == 1:
        screen.addstr(y, x - 5, exit_text[1])
        screen.attron(curses.color_pair(1))
        screen.addstr(y, x + 5, exit_text[2])
        screen.attroff(curses.color_pair(1))


def exit_screen(screen):
    screen.clear()
    selected_row_idx = 0
    exit_menu(screen, selected_row_idx)

    while True:
        key = screen.getch()

        if key == curses.KEY_RIGHT and selected_row_idx == 0:
            selected_row_idx += 1
            exit_menu(screen, selected_row_idx)
        if key == curses.KEY_LEFT and selected_row_idx == 1:
            selected_row_idx -= 1
            exit_menu(screen, selected_row_idx)
        if key == curses.KEY_ENTER or key in [10, 13]:
            if selected_row_idx == 0:
                exit()
            else:
                break
        screen.refresh()
    screen.clear()


def main_menu(screen, selected_row_idx):
    screen.clear()
    h, w = screen.getmaxyx()

    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, row)
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y, x, row)
    screen.refresh()


def print_center(screen, text):
    screen.clear()
    h, w = screen.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    screen.addstr(y, x, text)
    screen.refresh()


def main(screen):
    isExit = False

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0
    main_menu(screen, current_row)

    while not isExit:
        key = screen.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(menu) - 1:
                exit_screen(screen)
            elif current_row == len(menu) - 2:
                sudoku(screen, sudoku_blocks)
        main_menu(screen, current_row)

mixer.init()
mixer.music.load("game_musics/main_music.mp3")
mixer.music.play()
curses.wrapper(main)
