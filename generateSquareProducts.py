file = open("testingSets.txt", 'r')
integerSets = []

# integerSet contains all possible sidon sets generated from generateSidonSets.
# Format: integerSets[set index][index of num in set]
for lines in file:
    lines = lines.replace("{", "")
    lines = lines.replace("}", "")
    lines = lines.replace(",", "")
    lines = lines.replace("\n", "")
    lines = lines.split(" ")
    integerSets.append(lines)

# First possible sidonSet is: {1, 2, 4, 8, 9, 10}.
lambdaIndices = [0, 2, 3, 4]
# First lambda choices should be: {2, 8, 9, 10}.
lambdaChoices = []

'''# GATHER LAMBDA CHOICES
for index in lambdaIndices:
    lambdaChoices.append(integerSets[0][index - 1])'''

# FORM PRODUCT
# product 1
testIndices = [0, 2, 3, 4]
test = [1, 28, 33, 36, 43]
testChoices = [1, 33, 36, 43]
end = -1

productNums = []
totalProduct = 1

for index in range(0, len(testChoices)):
    if index + 1 > len(testChoices) - 1:
        diff = testChoices[index] - testChoices[testIndices[0]]
        productNums.append(diff)
        break
    diff = testChoices[index] - testChoices[index + 1]
    productNums.append(diff)

for nums in productNums:
    totalProduct *= nums

print(totalProduct)