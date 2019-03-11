import sys
import numpy as np

def initialise_matrix(num, coords, area):
    x, y = coords.rstrip(':').split(',')
    xlen, ylen = area.split('x')
    x, y, xlen, ylen = [int(i) for i in [x, y, xlen, ylen]]
    max_x = x + xlen
    max_y = y + ylen
    matrix = np.zeros((max_x, max_y))
    matrix[x:max_x, y:max_y] = 1
    return matrix.transpose()

def pad_matrix(m, x, y):
    if m.shape[0] < extent_x:
        m = np.vstack((m, np.zeros((extent_x - m.shape[0], m.shape[1]))))
    if m.shape[1] < extent_y:
        m = np.hstack((m, np.zeros((m.shape[0], extent_y - m.shape[1]))))
    return m

with open(sys.argv[1], 'r') as ofh:
    lines = ofh.read().splitlines()
    mlist = []
    for line in lines:
        num, _, coords, area = line.split(' ')
        mlist.append(initialise_matrix(num, coords, area))

extent_x = max([i.shape[0] for i in mlist])
extent_y = max([i.shape[1] for i in mlist])
pad_list = [pad_matrix(m, extent_x, extent_y) for m in mlist]

unique, counts = np.unique(np.sum(np.dstack(pad_list), axis = 2), return_counts=True)
results = dict(zip(unique, counts))
sum = 0
for k, v in results.items():
    if int(k) > 1:
        sum+=v
print(results)
print(f"\033[0;30;42mAnswer = {sum}\033[0m")

# Alternate padding strategy:
#
# ma,na = A.shape
# mb,nb = B.shape
# m,n = max(ma,mb) , max(na,nb)
#
# newA = np.zeros((m,n),A.dtype)
# newA[:ma,:na]=A
#
# newB = np.zeros((m,n),B.dtype)
# newB[:mb,:nb]=B
