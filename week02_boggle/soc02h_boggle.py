import numpy

test_mode = True

words_dict = {}
boggle_board = []

directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, -1]]

# ----------------------------------------------------- Main

def get_test_dictionary():
    return {
        'YES': True,
        'NO': True,
        'BIG': True,
        'SMALL': True,
        'SUN': True,
        'DO': True,
        'LET': True,
        'AND': True,
        'TABLE': True,
        'WINDOW': True,
        'EXERCISE': True
    }


def get_test_boggle_board():
    return [
        ['Y', 'X', 'C', 'R'],
        ['E', 'S', 'I', 'E'],
        ['D', 'M', 'U', 'X'],
        ['N', 'D', 'N', 'E']
    ]
    # return [
    #     ['Y', 'X', 'W', 'W', 'X'],
    #     ['E', 'S', 'i', 'O', 'S'],
    #     ['D', 'U', 'N', 'D', 'M'],
    #     ['N', 'X', 'T', 'E', 'A'],
    #     ['A', 'X', 'E', 'L', 'L']
    # ]



def load_dictionary():
    # TODO: load dictionary
    pass


def generate_buggle_board():
    # TODO: generate board
    pass


def is_word(word):
    return word in words_dict.keys()


def find_word(buggle_board, row, col, visited=[], found_words=[], w=''):
    # print(row, col, ':')
    if w == '':
        visited = numpy.zeros([len(buggle_board), len(buggle_board)])

    if 0 <= row < len(buggle_board) and 0 <= col < len(buggle_board) and not visited[row][col]:
        new_word = w + buggle_board[row][col]
        visited[row][col] = True

        if is_word(new_word):
            # save the word
            # print('Word found: ', new_word)
            found_words.append(new_word)

        for dir in directions:
                find_word(buggle_board, row + dir[0], col + dir[1], visited, words, new_word)

        visited[row][col] = False

    return found_words

# ----------------------------------------------------- Main


if test_mode:
    words_dict = get_test_dictionary()
    boggle_board = get_test_boggle_board()

else:
    words_dict = load_dictionary()
    boggle_board = generate_buggle_board()


# let's do the magic :)

words = []
# for row in range(0, len(boggle_board)):
#     for col in range(0, len(boggle_board)):

words += find_word(boggle_board, 0, 0)
words += find_word(boggle_board, 3, 3)
print(words)
