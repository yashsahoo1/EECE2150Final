from tkinter import *
from tkinter import font
from functools import partial

global choice1
choice1 = None
global choice2
choice2 = None
global w_bank
global buttons
global choice1_row
global choice1_col


def str_bank(word_bank):
    bank = ''

    bank += '\nWord Bank (' + str(len(word_bank)) + ' words remaining)\n\n'  # Print word bank
    for word in range(len(word_bank)):
        bank += "%-15s" % (word_bank[word])
        if word % 4 == 3:
            bank += '\n'
    return bank


def solve_ws(word_bank, dimension, search_array):

    root = Tk()
    root.title("Word Search!!")
    textfont = font.Font(family="consolas")
    textfont.config(size=8)

    global w_bank
    w_bank = word_bank

    bank = str_bank(word_bank)
    word_bank = Label(root, text=bank, font=textfont)
    word_bank.grid(row=0, column=0, rowspan=dimension)

    def click_letter(row, col):
        global choice1
        global choice2
        global choice1_row
        global choice1_col
        global w_bank
        global buttons
        print(search_array[row][col].value)
        print(search_array[row][col].parent)
        print(search_array[row][col].place_in_word)
        choice1 = choice2
        choice2 = search_array[row][col]
        if choice1 and choice2 and choice2.place_in_word and choice1.place_in_word and choice1 != choice2 \
                and choice1.parent == choice2.parent:
            w_bank.remove(choice2.parent)
            print("Removed")

            bank = str_bank(w_bank)
            word_bank = Label(root, text=bank, font=textfont)
            word_bank.grid(row=0, column=0, rowspan=dimension)

            if choice1.place_in_word == 'Start':
                start_x = choice1_col
                start_y = choice1_row
            else:
                start_x = col
                start_y = row

            if row == choice1_row:
                for column in range(min(col, choice1_col), max(col, choice1_col) + 1):
                    buttons[row][column].configure(bg="red", fg="yellow")
            elif col == choice1_col:
                for _row in range(min(row, choice1_row), max(row, choice1_row) + 1):
                    buttons[_row][col].configure(bg="red", fg="yellow")
            else:
                for increment in range(len(choice2.parent)):
                    buttons[start_y + choice1.dy*increment][start_x + choice1.dx*increment].configure(bg="red", fg="yellow")
        choice1_col = col
        choice1_row = row
        return

    global buttons
    buttons = [[None for x in range(dimension)] for x in range(dimension)]

    for r in range(dimension):
        for c in range(dimension):
            buttons[r][c] = Button(root, text=search_array[r][c].value, padx=5, pady=0,
                                   command=partial(click_letter, r, c), font=textfont)
            buttons[r][c].grid(row=r, column=c+20)

    root.mainloop()
