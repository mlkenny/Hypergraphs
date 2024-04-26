# FOR TESTING IMPLEMENTATIONS

import numpy as np
import pandas as pd

def main():
    file = open("testingSets.txt", 'r')
    girth = 4
    setSize = girth - 1
    integerSets = []

    for lines in file:
        lines = lines.replace("(", "")
        lines = lines.replace(")", "")
        lines = lines.replace(",", "")
        lines = lines.replace("\n", "")
        lines = lines.split(" ")
        integerSets.append(lines)
        
    file.close()

# girth = 4
# j (0, 3)
# i (1, 3 - j)
# set[girth - 1 - j] - set[girth - 1 - i - 0]

# set[4 - 1 - 0] - set[4 - 1 - 1 - 0] => set[3] - set[2]
# set[4 - 1 - 0] - set[4 - 1 - 2 - 0] => set[3] - set[1]
# set[4 - 1 - 0] - set[4 - 1 - 3 - 0] => set[3] - set[0]

# set[4 - 1 - 1] - set[4 - 1 - 1 - 1] => set[2] - set[1]
# set[4 - 1 - 1] - set[4 - 1 - 2 - 1] => set[2] - set[0]

# set[4 - 1 - 2] - set[4 - 1 - 1 - 2] => set[1] - set[0]
    
if __name__=="__main__": 
    main()