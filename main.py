from words import get_words
from analyze import *

if __name__ == '__main__':
    words = get_words()
    print(sort_dict(letter_freq(words)))
    print(sort_dict(letter_combo_freq(words, 2)))
    print(sort_dict(letter_combo_freq(words, 3)))
    print(sort_dict(letter_coincide(words, 2)))
    print(sort_dict(letter_coincide(words, 3)))
