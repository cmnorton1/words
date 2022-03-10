import string
from itertools import combinations, permutations


# Given a list of words, identify most common letters
def letter_freq(words):
    abc_string = string.ascii_lowercase
    freq_dist = {}
    for letter in abc_string:
        freq_dist[letter] = 0
    for word in words:
        for letter in word:
            freq_dist[letter] += 1
    return freq_dist


# Given a list of words, identify two letter combinations and provide frequency distribution
def letter_combo_freq(words, num_letters):
    freq_dist = {}
    abc_list = list(string.ascii_lowercase)
    # Formal permutation, order matters
    combos = list(permutations(abc_list, num_letters))
    # This line accounts for double letter incidences ex. 'oo' in 'goose'
    if num_letters == 2:
        for item in abc_list:
            combos.append((item, item))
    for combo in combos:
        combo_str = ""
        for i in range(0, num_letters):
            combo_str += combo[i]
        for word in words:
            if combo_str in word:
                if combo_str not in freq_dist.keys():
                    freq_dist[combo_str] = 1
                else:
                    freq_dist[combo_str] += 1

    return freq_dist


def letter_coincide(words, num_letters):
    freq_dist = {}
    abc_list = list(string.ascii_lowercase)
    # Formal combinations, order doesn't matter
    combos = list(combinations(abc_list, num_letters))
    for combo in combos:
        combo_str = ""
        for i in range(0, num_letters):
            combo_str += combo[i]
        for word in words:
            # This means set1 is a subset of set2, order doesn't matter
            if set(combo_str) <= set(word):
                if combo_str not in freq_dist.keys():
                    freq_dist[combo_str] = 1
                else:
                    freq_dist[combo_str] += 1

    return freq_dist


def sort_dict(xdict):
    xlist = sorted(xdict.items(), key=lambda x:x[1], reverse=True)
    return dict[xlist]