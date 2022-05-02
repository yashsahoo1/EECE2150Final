import random


class Letter:
    '''
    A class to represent a single letter on the word search board.  Contains data that is helpful during gameplay.
    '''

    def __init__(self):

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        random.seed()
        self.value = random.choice(alphabet)
        self.part_of_word = False
        self.place_in_word = None
        self.parent = None
        self.dy = None
        self.dx = None
        self.reverse = None
