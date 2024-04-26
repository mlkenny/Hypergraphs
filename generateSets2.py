from math import comb

girth = 6
# GENERATE ALL POSSIBLE SETS HERE
# Assume sets to be of girth 4 for now.
possibleSets = []
sidonSets = []
N = 50
x1 = 1
# {1, 2-100, 101-200, 201-300, ...}
for x2 in range(2, N + 1):
    for x3 in range(3, N + 1):
        for x4 in range(4, N + 1):
            for x5 in range(5, N + 1):
                for x6 in range(6, N + 1):
                    tuple = (x1, x2, x3, x4, x5, x6)
                    possibleSets.append(tuple)
                    # CHECK IF SET IS A SIDON SET
                    isSidonSet = True
                    for set in possibleSets:
                        i = girth - 1
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
print(sidonSets)