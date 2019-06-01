import argparse

def split_word(word):
    positions = [pos for pos, char in enumerate(word) if char in ['a', 'e', 'i', 'o', 'u']]

    res = []
    pos_ref = 0

    for pos in positions:
        res.append(word[pos_ref:pos])
        pos_ref = pos

    res.append(word[pos_ref:])

    print(res)

    return res

def arguments_parsing():
    """

    :return:
    """


    parser = argparse.ArgumentParser(description='split word')
    parser.add_argument("--split", required=True,
                        help="split the given name by vowels")

    args = parser.parse_args()

    return args

def split_theword():
    """

    :return:
    """
    args = arguments_parsing()
    split_word(args.split)

if __name__ == '__main__':
    split_theword()