from math import comb

girth = 4
# GENERATE ALL POSSIBLE SETS HERE
# Assume sets to be of girth 4 for now.
possibleSets = []
N = 100
x1 = 1
for x2 in range(2, N + 1):
    for x3 in range(N, N * 2 + 1):
        for x4 in range(N * 2, N * 3 + 1):
            tuple = (x1, x2, x3, x4)
            possibleSets.append(tuple)

# CHECK IF SET IS A SIDON SET
isSidonSet = True
sidonSets = []
for set in possibleSets:
    i = 3
    diffs = []
    while i >= 1 and isSidonSet:
        j = i - 1
        while j >= 0 and isSidonSet:
            difference = set[i] - set[j]
            if difference not in diffs:
                diffs.append(difference)
            else:
                isSidonSet = False
            j -= 1
        i -= 1
    if isSidonSet:
        sidonSets.append(set)