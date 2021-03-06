from tkinter import *
from tkinter import font
from functools import partial


class GameWindow:
    '''
    A class to represent the gameplay window that shows the user the wordsearch and allows for manipulation
    '''

    def __init__(self, word_bank, dimension, search_array, preferences):
        '''
        Creates Game window and executes game functions
        :param word_bank: List of words
        :param dimension: int -- size of search
        :param search_array: lst -- array of letters
        '''

        # Declare all necessary attributes

        self.word_bank = word_bank
        self.dimension = dimension
        self.search_array = search_array
        self.instructions = 'INSTRUCTIONS: \n\nTo cross a word off of the list, click one end of the \n word ' \
                            'and then the other end of the word, without clicking \nanything else' \
                            ' in between.\n\nPREFERENCES:\n\n-Size: ' + str(preferences[0]) + "\n-Diagonals: " \
                            + str(preferences[1]) + "\n-Reversed Words: " + str(preferences[2])

        # Attributes for selection of letters
        self.choice1 = None
        self.choice1_row = None
        self.choice1_col = None
        self.choice2 = None

        # GUI preferences attributes
        self.root = Tk()
        self.root.title("Word Search!!")
        self.text_font = font.Font(family="consolas")
        self.text_font.config(size=8)

        # Create buttons to display as wordsearch
        self.buttons = [[None for x in range(dimension)] for x in range(dimension)]
        self.set_buttons()

        # Create vars that will define the location of word bank
        self.wb_c = None
        self.wb_r = None
        self.wb_cs = None
        self.wb_rs = None

        # Calls function to output board and play
        self.start()

        # Run Tk()
        self.root.mainloop()

    def str_bank(self):
        '''
        Returns formatted string list of all remaining unfound words
        :return: str -- Remaining words to find
        '''

        # bank = self.instructions
        bank = ''
        bank += '\n\n\n\nWord Bank (' + str(len(self.word_bank)) + ' words remaining)\n\n'  # Print word bank
        for word in range(len(self.word_bank)):
            bank += "%-15s" % (self.word_bank[word])
            if word % 4 == 3:
                bank += '\n'
        if len(self.word_bank) % 4:
            for x in range(4-len(self.word_bank) % 4):
                bank += "%-15s" % ''
        return bank

    def start(self):
        '''
        Sets up initial board
        :return:
        '''

        w_bank = self.word_bank
        bank = self.str_bank()
        instructions = Label(self.root, text=self.instructions, font=self.text_font)

        if self.dimension > 10:
            instructions.grid(row=0, column=0, rowspan=3*self.dimension//4)
        else:
            instructions.grid(row=0, column=0, rowspan=self.dimension)

        word_bank = Label(self.root, text=bank, font=self.text_font)

        if self.dimension >= 20:
            self.wb_c = 0
            self.wb_cs = 1
            self.wb_r = self.dimension//2
            self.wb_rs = self.dimension
        else:
            self.wb_c = 1
            self.wb_cs = self.dimension*5
            self.wb_r = self.dimension+1
            self.wb_rs = 1
        word_bank.grid(row=self.wb_r, column=self.wb_c, columnspan=self.wb_cs, rowspan=self.wb_rs)

    def click_letter(self, row, col):
        '''
        Detects letter click, and carries out appropriate actions
        :param row:
        :param col:
        :return:
        '''

        print(self.search_array[row][col].value)
        print(self.search_array[row][col].parent)             # Debugging
        print(self.search_array[row][col].place_in_word)

        self.choice1 = self.choice2                            # Sets choice 1 and 2
        self.choice2 = self.search_array[row][col]

        # If choice 1 and 2 are start/end of word, execute this block of code
        if self.choice1 and self.choice2 and self.choice2.place_in_word and self.choice1.place_in_word \
                and self.choice1 != self.choice2 and self.choice1.parent == self.choice2.parent:

            # Removes found word from word list
            if self.choice1.reverse:
                self.word_bank.remove(self.choice2.parent[::-1])
            else:
                self.word_bank.remove(self.choice2.parent)
            print("Removed")

            # Recreates word bank string and re-displays
            bank = self.str_bank()
            word_bank = Label(self.root, text=bank, font=self.text_font)
            word_bank.grid(row=self.wb_r, column=self.wb_c, columnspan=self.wb_cs, rowspan=self.wb_rs)
            # instructions = Label(self.root, text=self.instructions, font=self.text_font)
            # instructions.grid(row=0, column=0, columnspan=self.dimension)

            # Determines start of word
            if self.choice1.place_in_word == 'Start':
                start_x = self.choice1_col
                start_y = self.choice1_row
            else:
                start_x = col
                start_y = row

            # Iterates through letters in word and disables those buttons, turning them red
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

            # If all words are found, the screen is cleared, and it displays a "You win" message
            if len(self.word_bank) == 0:
                for widget in self.root.winfo_children():
                    widget.destroy()
                text_font = font.Font(family="Times")
                text_font.config(size=100)
                win = Label(self.root, text='YOU WIN!', font=text_font)
                win.grid(row=0, column=0, rowspan=2*self.dimension, columnspan=self.dimension)

        self.choice1_col = col
        self.choice1_row = row
        return

    def set_buttons(self):
        '''
        Creates the button objects that compose the board
        :return:
        '''

        for r in range(self.dimension):
            for c in range(self.dimension):
                self.buttons[r][c] = Button(self.root, text=self.search_array[r][c].value, padx=5, pady=0,
                                            command=partial(self.click_letter, r, c), font=self.text_font)
                self.buttons[r][c].grid(row=r+1, column=c+1)
