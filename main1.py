from play_game import GameWindow
from wordsearch import WordSearch
from inputwindow import InputWindow

Input = InputWindow()

Word_Search_Obj = WordSearch('dict.txt', Input.selectionsize, Input.selectiondiag, Input.reverse)

print(Input.selectionsize, '\n', Word_Search_Obj, sep='')

Word_Search_Obj.print_txt_file()

Gameplay = GameWindow(Word_Search_Obj.word_list, Word_Search_Obj.dimension, Word_Search_Obj.search_array)
