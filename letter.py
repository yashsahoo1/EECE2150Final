import random


class Letter:

    def __init__(self):

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.value = random.choice(alphabet)
        self.part_of_word = False
