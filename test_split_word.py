import split_word

def test_split():
    """

    :return:
    """
    wordsplit = split_word.split_word("test_split")
    assert (wordsplit == ['D', 'ej', 'an'])