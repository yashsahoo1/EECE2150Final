from wordsearch import WordSearch


print("General check")

for x in range(10, 15):

    CheckWordSearchCreation = WordSearch('dict.txt', x)
    # print("Dimension:\n", CheckWordSearchCreation.get_answer_key(), sep='')

print("Diags: ")

for x in range(20, 30):
    Diags = WordSearch('dict.txt', x, True)
    print(Diags.get_answer_key())

for x in range(20, 30):
    Reverse = WordSearch('dict.txt', x, False, True)
    print(Reverse.get_answer_key())

for x in range(20, 30):
    CheckWordDeletionWithOverload = WordSearch('dict.txt', x, False, False, 100)
    print(CheckWordDeletionWithOverload.get_answer_key())

