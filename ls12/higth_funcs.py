WORD_LIST = 'паук', "кот", "собака", "жираф"

def less_len(word):
    return len(word) <= 4


def word_len(word):
    return len(word)

resl = list(filter(less_len, WORD_LIST))
print(resl)


resl2 = list(map(word_len, WORD_LIST))
print(resl2)

