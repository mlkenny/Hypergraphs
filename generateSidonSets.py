'''
Generate all possible sets in the range: {1, 2, 3, 4, 5, 6} to {1, N-4, N-3, N-2, N-1, N}.
All possible sets are checked at girth 4 for the sidon set property. This eliminates reundant calculations.
'''
### Assume sets to be of girth 6.

## Arrays to hold sets for evaluation and comparison.
# possibleSets are checked at girth 4 for the sidon set property.
# sidonSets contains all sidon sets of N for range {1, 2->N-4, 3->N-3, 4->N-2, 5->N-1, 6->N}
possibleSets = []
sidonSets = []
sidonNumber = 0
possibleNumber = 0

N = 30
## Assume possible sets were not checked for sidon set property.
# N = 10; 126 total possible sets; 0 sidon sets.
# N = 20; 11,628 total possible sets; 56 sidon sets.
# N = 30; 118,755 total possible sets; 9,968 sidon sets.
# N = 40; 575,757 total possible sets; 111,202 sidon sets.
# N = 50; 1,906,885 total possible sets; 555,384 sidon sets.
# N = 100; 41,223,580 sidon sets.
## After checking for sidon set property at girth 4.
# N = 10; 12 possible sets  -   9.5% difference
# N = 20; 5,876 possible sets   -   50.5% difference
# N = 30; 79,248 possible sets  -   66.7% difference
# N = 40; 431,796 possible sets -   74.9% difference
# N = 50; 1,525,184 possible sets   -   79.9% difference
# N = 100; 64,363,088 possible sets.

# OPEN FILE
file = open("setsOutput.txt", 'w')

file.write("All possible sets have passed the sidon set property check at girth 4.\n")
file.write("\nList of all possible sets of N = " + str(N) + ", where all sets are in the range of:\n{{1, (2, N-4), (3, N-3), (4, N-2), (5, N-1), (6, N)}}.".format() + "\n**This is truly an overcount as we only consider sets that pass the sidon set property at girth 4.**\n")
file.write("\nCtrl+F search 'sidon set' to find possible sidon sets and to check number of sidon sets and number of possible sets when N = " + str(N) + ".\n")
file.write("\nAll possible sets of girth 6:\n") # comment this out if you are checking high N values.

# GENERATE POSSIBLE SETS
x1 = 1
for x2 in range(2, N + 1):
    for x3 in range(3, N + 1):
        # check if x2 and x3 are increasing and distinct.
        # if not, then skip number.
        if x2 >= x3:
            pass
        else:
            for x4 in range(4, N + 1):
                # check if x3 and x4 are increasing and distinct.
                # if not, then skip number.
                if x3 >= x4:
                    pass
                else:
                    tempTuple = (x1, x2, x3, x4)
                    # SIDON SET PROPERTY CHECK AT GIRTH 4
                    isSidonSet = True
                    i = 3
                    diffs = []
                    # check differences.
                    while i >= 1:
                        j = i - 1
                        while j >= 0:
                            # find each difference between all elements.
                            difference = tempTuple[i] - tempTuple[j]
                            if difference not in diffs:
                                # if difference is unique, add it to list.
                                diffs.append(difference)
                            else:
                                # if difference is not unique, it is not a sidon set.
                                isSidonSet = False
                                break
                            j -= 1
                        if not isSidonSet:
                            break
                        i -= 1
                    # if not a sidon set, go to next x4.
                    if not isSidonSet:
                        continue
                    for x5 in range(5, N + 1):
                        # check if x4 and x5 are increasing and distinct.
                        # if not, then skip number.
                        if x4 >= x5:
                            pass
                        else:
                            for x6 in range(6, N + 1):
                                # check if x5 and x6 are increasing and distinct.
                                # if not, then skip number.
                                if x5 >= x6:
                                    pass
                                else:
                                    # if loop reaches here then tuple will have property of:
                                    # 1 < x2 < x3 < x4 < x5 < x6
                                    tuple = tempTuple + (x5, x6)
                                    possibleSets.append(tuple)
                                    possibleNumber += 1
                                    # WRITE POSSIBLE SETS TO FILE
                                    # comment out if using high values of N.
                                    count = len(tuple) - 1
                                    string = '{'
                                    for char in tuple:
                                        if count == 0:
                                            string = string + str(char) + '},\n'
                                            break
                                        else:
                                            string = string + str(char) + ', '
                                            count -= 1
                                    file.write(string)

# CHECK IF SET IS A SIDON SET
# the first 4 elements of the set exhibit the sidon set property; is there a way to not have to recheck those subtractions? not optimized.
file.write("\nList of all sidon sets from possible sets of girth 6:\n")
for set in possibleSets:
    isSidonSet = True
    i = len(set) - 1
    diffs = []
    while i >= 1:
        if not isSidonSet:
            break
        j = i - 1
        while j >= 0:
            difference = set[i] - set[j]
            if difference not in diffs:
                diffs.append(difference)
            else:
                isSidonSet = False
                break
            j -= 1
        i -= 1
    if isSidonSet:
        # if loop reaches here then set will have the property of a sidon set.
        sidonSets.append(set)
        sidonNumber += 1
        # write sidon sets to file.
        count = len(set) - 1
        string = '{'
        for char in set:
            if count == 0:
                string = string + str(char) + '},\n'
                break
            else:
                string = string + str(char) + ', '
                count -= 1
        file.write(string)

# WRITE NUMERICAL DATA TO FILE
file.write("\nThere are " + str(possibleNumber) + " possible sets that pass the sidon set property at girth 4 when N = " + str(N))
file.write("\nThere are " + str(sidonNumber) + " sidon sets when N = " + str(N))
file.close()