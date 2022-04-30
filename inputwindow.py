from tkinter import *


class InputWindow:

    def __init__(self):
        print("Here")
        self.selectionsize = None
        self.selectiondiag = None
        self.reverse = None
        self.window = Tk()
        self.window.title("Wordsearch Generator! ")
        self.window.geometry("500x500")
        self.buttonclick = None
        self.buttonclick2 = None
        self.buttonclick3 = None
        self.make_buttons()

    def make_buttons(self):
        # part1
        gridoptions = {

            "10x10": 10,
            "15x15": 15,
            "20x20": 20,
            "25x25": 25,
            "30x30": 30,
            "35x35": 35

        }

        self.buttonclick = StringVar()
        self.buttonclick.set("Gridsize")
        dropdown = OptionMenu(self.window, self.buttonclick, *gridoptions)
        dropdown.pack()

        # part 2
        diagonaloptions = {

            "Yes": 1,
            "No": 0
        }

        self.buttonclick2 = StringVar()
        self.buttonclick2.set("Include Diagonal? ")

        dropdown2 = OptionMenu(self.window, self.buttonclick2, *diagonaloptions)
        dropdown2.pack(pady=20)

        # part 3
        reverseoptions = {
            "Yes": 1,
            "No": 0
        }

        self.buttonclick3 = StringVar()
        self.buttonclick3.set("Reverse Character? ")

        dropdown3 = OptionMenu(self.window, self.buttonclick3, *reverseoptions)
        dropdown3.pack()

        # button
        button1 = Button(self.window, text="Generate Wordsearch", command=self.selection)
        button1.pack(pady=50)
        self.window.mainloop()

    def selection(self):

        self.selectionsize = self.buttonclick.get()

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
        elif self.selectionsize == "40x40":
            self.selectionsize = 40
        elif self.selectionsize == "45x45":
            self.selectionsize = 45
        elif self.selectionsize == "50x50":
            self.selectionsize = 50

        # print(selectionsize)

        selectiondiag = self.buttonclick2.get()
        if selectiondiag == "No":
            selectiondiag = False
        elif selectiondiag == "Yes":
            selectiondiag = True

        # print(selectiondiag)

        reverse = self.buttonclick3.get()
        if reverse == "Yes":
            reverse = True
        elif reverse == "No":
            reverse = False

        self.window.destroy()