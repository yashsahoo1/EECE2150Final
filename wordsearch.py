
import copy
import random
from letter import Letter

random.seed()


class WordSearch:
    '''
    A class to represent the basic Word Search object
    '''

    def __init__(self, word_file_path='dict.txt', dimension=10, diagonal=False, reverse=False, override_word_count=-1):
        '''
        Creates Word Search Object
        :param word_file_path: String describing file path that refers to a text file holding list of words
        :param dimension: int (nxn wordsearch created)
        :param diagonal: bool  True if diagonals are allowed
        :param reverse: bool  True if reversing words is allowed
        '''

        self.dimension = dimension  # add parameters as object attributes

        if dimension < 5:
            raise ValueError("The minimum dimension for a wordsearch is 5x5")

        self.reverse = reverse

        self.num_words = 8*1.06**(dimension - 10)
        # use dimension size and a determined model to find wordcount
        if override_word_count > 0:
            self.num_words = override_word_count

        self.max_word_len = dimension-2  # restrict word length based off of dimension of word search
        self.min_word_len = 3  # words in wordsearch must be at least three letters

        # generate a list of words given the above metrics
        self.word_list = get_words(word_file_path, self.max_word_len, self.num_words, self.min_word_len)

        # if diagonals are allowed, add corresponding directions to the possible directions
        self.parameters = ['Horiz', 'Vert']
        if diagonal:
            self.parameters.append('Diag')          # Word starts top left and goes downward and right
            self.parameters.append('Rev_Diag')      # Word starts top right and goes downward and left

        # Initialize arrays that show locations of words
        self.search_array = []

        self.hide_words()   # Hide the words from word_list in the wordsearch

    def __str__(self):
        '''
        Returns printable format of Wordsearch
        :return: String representation of Wordsearch object
        '''

        string_output = ''    # Initialize

        for x in range(self.dimension):         # Print word search array
            for y in range(self.dimension):
                string_output += self.search_array[x][y].value + '  '
            string_output += '\n'

        string_output += '\nWord Bank: \n\n'       # Print word bank
        for word in range(len(self.word_list)):
            string_output += "%-15s" % (self.word_list[word])
            if word % 4 == 3:
                string_output += '\n'
        return string_output

    def hide_words(self):
        '''
        Populates the search array, hiding words within and generating answer key
        :return:
        '''

        # Initialize the search array, answer key array, and the placement array (useful when validating placements)

        # Search array set to random letters by default
        self.search_array = [[Letter() for x in range(self.dimension)] for y in range(self.dimension)]

        for word in self.word_list:

            placed = False  # Set placement signifier to unplaced
            fail = 0  # Set fail count to 0

            reverse = 0  # Sets default value for reversal to 0 signifying un-reversed

            if self.reverse:
                reverse = random.randrange(0, 2)   # If reversed words enabled, recalculate whether reversed

            if reverse:
                word = word[::-1]    # If reversed, reverse word

            while not placed:

                # Create temporary versions of the different arrays to alter without influencing the actual versions
                # before these alterations are determined to be valid
                temp_array = copy.deepcopy(self.search_array)

                direction = random.choice(self.parameters)  # Choose direction from the possible pool created in __init_

                dx = 0
                dy = 0

                # Set the correct values for dy and dx that will be used to increment during letter placement
                if direction == 'Horiz':
                    dx = 1
                    dy = 0
                elif direction == 'Vert':
                    dx = 0
                    dy = 1
                elif direction == 'Diag':
                    dx = 1
                    dy = 1
                elif direction == 'Rev_Diag':
                    dx = 1
                    dy = 1  # *** This value is falsely valued at 1, will be accounted for later ***

                # Choose a valid starting position based off of the word length and both dy and dx
                x = random.randint(0, (self.dimension-1) - len(word)*dx)
                y = random.randint(0, (self.dimension-1) - len(word)*dy)

                if direction == 'Rev_Diag':
                    y = (self.dimension-1)-y  # Reflect vertically the starting position
                    dy = -1   # Reverse the dy value --> These changes create the upward and right direction

                placed = True   # Set default placement identifier to True (if it fails this will be changed)

                for letter in range(len(word)):

                    # If the space does not contain a word already, place the letter
                    # updates the search, answer, and placement indicator arrays
                    if not temp_array[y][x].part_of_word:
                        temp_array[y][x].value = word[letter]
                        temp_array[y][x].part_of_word = True
                        temp_array[y][x].parent = word

                        if not letter:
                            temp_array[y][x].place_in_word = 'Start'
                            temp_array[y][x].dy = dy
                            temp_array[y][x].dx = dx
                            temp_array[y][x].reverse = reverse

                        elif letter == len(word)-1:
                            temp_array[y][x].place_in_word = 'End'
                            temp_array[y][x].dy = dy
                            temp_array[y][x].dx = dx
                            temp_array[y][x].reverse = reverse

                        x += dx
                        y += dy
                    else:
                        # If this placement fails, break and try again
                        placed = False
                        break
                if placed:
                    # If the word was correctly placed, update each of the arrays
                    self.search_array = temp_array
                else:
                    # If it did fail, increment the fail counter
                    fail += 1
                    if fail > 10:
                        # If the word fails to be placed 20 times in a row, remove that word from the word list
                        if reverse:
                            print("del", word[::-1])
                            self.word_list.remove(word[::-1])
                        else:
                            print("del", word)
                            self.word_list.remove(word)
                        break
        return

    def get_answer_key(self):
        '''
        Returns an easy to interpret version of the word search's answer key
        :return: str representation of the answer key list
        '''
        write_ans_key = ''

        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.search_array[x][y].part_of_word:
                    write_ans_key += self.search_array[x][y].value + '  '
                else:
                    write_ans_key += '-' + '  '
            write_ans_key += '\n'
            # print(write_ans_key)
        return write_ans_key

    def print_txt_file(self):
        '''
        Sends the word search to one text file and the answer key to another
        :return:
        '''
        with open('Word_Search.txt', 'w') as f:
            print(self, file=f)
        with open('Word_Search_Answer_Key.txt', 'w') as f:
            print(self.get_answer_key(), file=f)


def get_words(file_path, max_length, num_words, min_length):
    '''
    Takes in a list of words and parameters for words to be selected from these words, returning a list of such words
    :param file_path: str
    :param max_length: int
    :param num_words: int
    :param min_length: int
    :return: list of randomly selected words that match criteria
    '''

    dictionary = open(file_path)
    words = dictionary.readlines()   # Gets lst of the possible words
    chosen_words = []  # Initializes list
    dictionary.close()

    while len(chosen_words) < num_words:
        # Chooses and formats word
        new_word = random.choice(words)
        words.remove(new_word)
        new_word = new_word.strip().upper()

        # If it qualifies, add to the list
        if min_length < len(new_word) <= max_length:
            chosen_words.append(new_word)
    return chosen_words
