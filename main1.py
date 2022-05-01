from gamewindow import GameWindow
from wordsearch import WordSearch
from inputwindow import InputWindow


# Brings up input window to get input from user regarding word search parameters
Input = InputWindow()


# Creates word search from given preferences
Word_Search_Obj = WordSearch('dict.txt', Input.selectionsize, Input.selectiondiag, Input.reverse)


print(Input.selectionsize, '\n', Word_Search_Obj, sep='')


# Sends word search and its answer key to two different text files
Word_Search_Obj.print_txt_file()


# Solve word search window
Gameplay = GameWindow(Word_Search_Obj.word_list, Word_Search_Obj.dimension, Word_Search_Obj.search_array,
                      (Input.selectionsize, Input.selectiondiag, Input.reverse))
