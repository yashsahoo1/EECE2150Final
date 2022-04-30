from wordsearch import WordSearch
from tkinter import *
from play_game import GameWindow

selectionsize = 0
selectiondiag = 0
reverse = 0


def selection():
    global selectionsize
    global selectiondiag
    global reverse
    selectionsize = buttonclick.get()

    if selectionsize == "10x10":
        selectionsize = 10
    elif selectionsize == "15x15":
        selectionsize = 15
    elif selectionsize == "20x20":
        selectionsize = 20
    elif selectionsize == "25x25":
        selectionsize = 25
    elif selectionsize == "30x30":
        selectionsize = 30
    elif selectionsize == "35x35":
        selectionsize = 35
    elif selectionsize == "40x40":
        selectionsize = 40
    elif selectionsize == "45x45":
        selectionsize = 45
    elif selectionsize == "50x50":
        selectionsize = 50

    #print(selectionsize)

    selectiondiag = buttonclick2.get()
    if selectiondiag == "No":
        selectiondiag = False
    elif selectiondiag == "Yes":
        selectiondiag = True

    #print(selectiondiag)

    reverse = buttonclick3.get()
    if reverse == "Yes":
        reverse = True
    elif reverse == "No":
        reverse = False

    wordsearch.destroy()


wordsearch = Tk()
wordsearch.title("Wordsearch Generator! ")
wordsearch.geometry("500x500")

# part1
gridoptions = {

    "10x10": 10,
    "15x15": 15,
    "20x20": 20,
    "25x25": 25,
    "30x30": 30,
    "35x35": 35

}

buttonclick = StringVar()
buttonclick.set("Gridsize")
dropdown = OptionMenu(wordsearch, buttonclick, *gridoptions)
dropdown.pack()

# part 2
diagonaloptions = {

    "Yes": 1,
    "No": 0
}

buttonclick2 = StringVar()
buttonclick2.set("Include Diagonal? ")

dropdown2 = OptionMenu(wordsearch, buttonclick2, *diagonaloptions)
dropdown2.pack(pady=20)

# part 3
reverseoptions = {
    "Yes": 1,
    "No": 0
}

buttonclick3 = StringVar()
buttonclick3.set("Reverse Character? ")

dropdown3 = OptionMenu(wordsearch, buttonclick3, *reverseoptions)
dropdown3.pack()

# button
button1 = Button(wordsearch, text="Generate Wordsearch", command=selection)
button1.pack(pady=50)

wordsearch.mainloop()

w = WordSearch('dict.txt', selectionsize, selectiondiag, reverse)
print(selectionsize, '\n', w, sep='')

w.print_txt_file()

W = GameWindow(w.word_list, w.dimension, w.search_array)
