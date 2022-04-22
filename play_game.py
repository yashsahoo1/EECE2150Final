from tkinter import *
from tkinter import font


def solve_ws(word_bank, dimension, search_array):

    root = Tk()
    root.title("Word Search!!")
    textfont = font.Font(family="consolas")
    textfont.config(size=8)
    bank = ''

    bank += '\nWord Bank: \n\n'  # Print word bank
    for word in range(len(word_bank)):
        bank += "%-15s" % (word_bank[word])
        if word % 4 == 3:
            bank += '\n'

    word_bank = Label(root, text=bank, font=textfont)
    word_bank.grid(row=0, column=0, rowspan=dimension)

    def button_click():
        return

    buttons = [[None for x in range(dimension)] for x in range(dimension)]

    for r in range(dimension):
        for c in range(dimension):
            buttons[r][c] = Button(root, text=search_array[r][c].value, padx=5, pady=0, command=button_click, font=textfont)
            buttons[r][c].grid(row=r, column=c+20)


    root.mainloop()
