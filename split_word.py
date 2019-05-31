
def split_word(word):
    positions = [pos for pos, char in enumerate(word) if char in ['a', 'e', 'i', 'o', 'u']]
    print(positions)

    res = []
    pos_ref = 0

    for pos in positions:
        res.append(word[pos_ref:pos])
        pos_ref = pos

    res.append(word[pos_ref:])

    print(res)

split_word('Dejan')