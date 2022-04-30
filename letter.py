import random


class Letter:
    '''

    '''

    def __init__(self):

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.value = random.choice(alphabet)
        self.part_of_word = False
        self.place_in_word = None
        self.parent = None
        self.dy = None
        self.dx = None
        self.reverse = None
