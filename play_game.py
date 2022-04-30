from tkinter import *
from tkinter import font
from functools import partial


class GameWindow:

    def __init__(self, word_bank, dimension, search_array):
        self.word_bank = word_bank
        self.dimension = dimension
        self.search_array = search_array
        self.choice1 = None
        self.choice1_row = None
        self.choice1_col = None
        self.choice2 = None
        self.root = Tk()
        self.root.title("Word Search!!")
        self.text_font = font.Font(family="consolas")
        self.text_font.config(size=8)
        self.buttons = [[None for x in range(dimension)] for x in range(dimension)]
        self.set_buttons()
        self.solve_ws()
        self.root.mainloop()

    def str_bank(self):
        bank = ''
        bank += '\nWord Bank (' + str(len(self.word_bank)) + ' words remaining)\n\n'  # Print word bank
        for word in range(len(self.word_bank)):
            bank += "%-15s" % (self.word_bank[word])
            if word % 4 == 3:
                bank += '\n'
        if len(self.word_bank) % 4:
            for x in range(4-len(self.word_bank) % 4):
                bank += "%-15s" % ''
        return bank

    def solve_ws(self):

        w_bank = self.word_bank
        bank = self.str_bank()
        word_bank = Label(self.root, text=bank, font=self.text_font)
        word_bank.grid(row=0, column=0, rowspan=self.dimension)

    def click_letter(self, row, col):

        print(self.search_array[row][col].value)
        print(self.search_array[row][col].parent)
        print(self.search_array[row][col].place_in_word)
        self.choice1 = self.choice2
        self.choice2 = self.search_array[row][col]
        if self.choice1 and self.choice2 and self.choice2.place_in_word and self.choice1.place_in_word \
                and self.choice1 != self.choice2 and self.choice1.parent == self.choice2.parent:
            if self.choice1.reverse:
                self.word_bank.remove(self.choice2.parent[::-1])
            else:
                self.word_bank.remove(self.choice2.parent)
            print("Removed")

            bank = self.str_bank()

            word_bank = Label(self.root, text=bank, font=self.text_font)
            word_bank.grid(row=0, column=0, rowspan=self.dimension)

            if self.choice1.place_in_word == 'Start':
                start_x = self.choice1_col
                start_y = self.choice1_row
            else:
                start_x = col
                start_y = row

            if row == self.choice1_row:
                for column in range(min(col, self.choice1_col), max(col, self.choice1_col) + 1):
                    self.buttons[row][column].configure(bg="red", fg="yellow")
                    self.buttons[row][column]["state"] = DISABLED
            elif col == self.choice1_col:
                for _row in range(min(row, self.choice1_row), max(row, self.choice1_row) + 1):
                    self.buttons[_row][col].configure(bg="red", fg="yellow")
                    self.buttons[_row][col]["state"] = DISABLED
            else:
                for increment in range(len(self.choice2.parent)):
                    self.buttons[start_y + self.choice1.dy*increment][start_x + self.choice1.dx*increment].configure(bg="red", fg="yellow")
                    self.buttons[start_y + self.choice1.dy*increment][start_x + self.choice1.dx*increment]["state"] = DISABLED

        self.choice1_col = col
        self.choice1_row = row
        return

    def set_buttons(self):
        for r in range(self.dimension):
            for c in range(self.dimension):
                self.buttons[r][c] = Button(self.root, text=self.search_array[r][c].value, padx=5, pady=0,
                                            command=partial(self.click_letter, r, c), font=self.text_font)
                self.buttons[r][c].grid(row=r, column=c+20)
