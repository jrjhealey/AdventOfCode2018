import sys
from collections import Counter

with open(sys.argv[1], 'r') as fh:
    ids = fh.read().splitlines()
    freq = {}
    checksum = [0, 0]
    for i in ids:
        freq[i] = Counter(i)
        common = [j for i, j in Counter(i).most_common()]
        if 3 in common:
            checksum[0]+=1
        if 2 in common:
            checksum[1]+=1

for k, v in freq.items():
    print(f"\033[1;30;47m{k}\033[0m -> {v}")

print(f"\033[0;30;42mAnswer = {checksum[0]*checksum[1]}\033[0m")
