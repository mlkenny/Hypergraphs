def main():
    file = open("testingSets.txt", 'a')
    generateSets(file, 10, 20, 30)
    file.close()

def writeSets(file, set):
    file.write('{}\n'.format(set))

# Only able to generate sets of size 4.
def generateSets(file, x_2, x_3, x_4):
    for i in range (2, x_2 + 1):
        for j in range(x_2, x_3 + 1):
            for k in range(x_3, x_4 + 1):
                set = (1, i, j, k)
                writeSets(file, set)

if __name__=="__main__": 
    main()