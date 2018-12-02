import sys
with open(sys.argv[1], 'r') as fh:
    t = fh.read().splitlines()

seen = set()
sum = 0
found = False
iter = 1


while not found:
    iter+=1
    for i, num in enumerate(t):
        sum+=int(num)
        print(f"\033[1;30;47m Iteration \033[0m {iter:>4}:{i:<4} -> "
              f"Number = \033[1;31;40m{num:>7}\033[0m, "
              f"Sum = \033[1;32;40m{sum:<9}\033[0m")
        if sum in seen:
            print(f"\033[0;30;42mFirst duplicated incremental sum = {sum}\033[0m")
            found = True
            break
        else:
            seen.add(sum)
