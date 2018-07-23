

test_mode = True

words_dict = {}
boggle_board = []


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
        ['Y', 'X', 'W', 'W', 'X'],
        ['E', 'S', 'i', 'O', 'S'],
        ['D', 'U', 'N', 'D', 'M'],
        ['N', 'X', 'T', 'E', 'A'],
        ['A', 'X', 'E', 'L', 'L'],
    ]


def load_dictionary():
    # TODO: load dictionary into  words_dict
    return fill_test_words()
    pass


def generate_buggle_board():
    # TODO: generate board
    return get_test_boggle_board()
    pass


# ----------------------------------------------------- Main

if test_mode:
    words_dict = get_test_dictionary()
    boggle_board = get_test_boggle_board()

else:
    words_dict = load_dictionary()
    boggle_board = generate_buggle_board()


# let's do the magic :)

print(words_dict)
print(boggle_board)
