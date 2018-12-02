import sys
from itertools import combinations

def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

with open(sys.argv[1], 'r') as fh:
    ids = fh.read().splitlines()
    for each in combinations(ids, 2):
        if hamming_distance(each[0], each[1]) == 1:
            print(f"\033[0;30;42mAnswer = {each[0]} and {each[1]}\033[0m")
            print(f"\033[0;30;42mCommon = {''.join([char1 for char1, char2 in zip(each[0],each[1]) if char1 == char2])}\033[0m")
