import sys

with open(sys.argv[1], 'r') as fh:
    t = fh.read().splitlines()

numbers = map(int, t)
print(str(sum(numbers)))
