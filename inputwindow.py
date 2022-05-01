from tkinter import *


class InputWindow:
    '''
    A class that creates a GUI input window and stores user input regarding word search parameters
    '''

    def __init__(self):
        '''
        Creates necessary attributes and sets up input window
        '''

        # Create necessary attributes

        # Three main variables that will be useful for main1.py
        self.selectionsize = None
        self.selectiondiag = None
        self.reverse = None

        # Create display window
        self.window = Tk()
        self.window.title("Wordsearch Generator! ")
        self.window.geometry("500x500")

        # Create empty objects to hold buttons
        self.buttonclick = None
        self.buttonclick2 = None
        self.buttonclick3 = None

        # Create button objects
        self.make_buttons()

    def make_buttons(self):
        '''
        A method that specifically creates the buttons on the GUI screen
        :return:
        '''

        # List of options for size dropdown menu

        gridoptions = {

            "10x10": 10,
            "15x15": 15,
            "20x20": 20,
            "25x25": 25,
            "30x30": 30,
            "35x35": 35

        }

        # Create dropdown
        self.buttonclick = StringVar()
        self.buttonclick.set("Gridsize")
        dropdown = OptionMenu(self.window, self.buttonclick, *gridoptions)
        dropdown.pack()

        # List of options for diagonal dropdown menu

        diagonaloptions = {

            "Yes": 1,
            "No": 0
        }

        # Create dropdown

        self.buttonclick2 = StringVar()
        self.buttonclick2.set("Include Diagonal? ")

        dropdown2 = OptionMenu(self.window, self.buttonclick2, *diagonaloptions)
        dropdown2.pack(pady=20)

        # List of options for reverse dropdown menu

        reverseoptions = {
            "Yes": 1,
            "No": 0
        }

        # Create dropdown

        self.buttonclick3 = StringVar()
        self.buttonclick3.set("Reverse Character? ")
        dropdown3 = OptionMenu(self.window, self.buttonclick3, *reverseoptions)
        dropdown3.pack()

        # Create Generate word search button
        button1 = Button(self.window, text="Generate Wordsearch", command=self.selection)
        button1.pack(pady=50)

        # Run mainloop of window
        self.window.mainloop()

    def selection(self):
        '''
        A function that takes the input from the GUI window and stores it into class attributes
        :return:
        '''

        # Use input to generate selection size variable

        self.selectionsize = self.buttonclick.get()
        if self.selectionsize == "Gridsize":
            self.selectionsize = 10
        if self.selectionsize == "10x10":
            self.selectionsize = 10
        elif self.selectionsize == "15x15":
            self.selectionsize = 15
        elif self.selectionsize == "20x20":
            self.selectionsize = 20
        elif self.selectionsize == "25x25":
            self.selectionsize = 25
        elif self.selectionsize == "30x30":
            self.selectionsize = 30
        elif self.selectionsize == "35x35":
            self.selectionsize = 35

        print(self.selectionsize)

        # Use input to determine and store diagonal preference

        self.selectiondiag = self.buttonclick2.get()
        if self.selectiondiag == "Include Diagonal? ":
            self.selectiondiag = False
        if self.selectiondiag == "No":
            self.selectiondiag = False
        elif self.selectiondiag == "Yes":
            self.selectiondiag = True

        print(self.selectiondiag)

        # Use input to determine and store reverse preference

        self.reverse = self.buttonclick3.get()
        if self.reverse == "Reverse Character? ":
            self.reverse = False
        if self.reverse == "Yes":
            self.reverse = True
        elif self.reverse == "No":
            self.reverse = False

        print(self.reverse)

        # Closes input window
        self.window.destroy()
