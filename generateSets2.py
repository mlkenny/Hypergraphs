def isSidonSet(tuple):
    diffs = []
    end = len(tuple) - 1
    while(end != 0):
        for i in range(end):
            diffs.append(tuple[end] - tuple[end - i - 1])
            print(diffs)
        end -= 1

N = 100
x1 = 1
for x2 in range(2, N + 1):
    for x3 in range(N, N * 2 + 1):
        for x4 in range(N * 2, N * 3 + 1):
            tuple = (x1, x2, x3, x4)
            isSidonSet(tuple)