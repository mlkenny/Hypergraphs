from random import randint

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

def chooseFour(set):
    lambdaIndices = []
    while len(lambdaIndices) < 4:
        index = randint(0, len(set) - 1)
        if index not in lambdaIndices:
            lambdaIndices.append(index)
    lambdaChoices = []
    for index in range(0, len(lambdaIndices)):
        lambdaChoices.append(set[lambdaIndices[index]])
    return lambdaChoices

def formPositiveProducts(lambdaChoices):
    positiveProducts = []
    # FORM PRODUCT 1
    productNums = []
    totalProduct = 1
    for index in range(0, len(lambdaChoices)):
        if index + 1 > len(lambdaChoices) - 1:
            '''
            from chosen lambdas 1, 3, 4, 5
            create 4 differences:
            # (1-3)(3-4)(4-5)(5-1)
            (0-1)(1-2)(2-3)(3-0)
            '''
            diff = int(lambdaChoices[index]) - int(lambdaChoices[0])
            productNums.append(diff)
            break
        diff = int(lambdaChoices[index]) - int(lambdaChoices[index + 1])
        productNums.append(diff)
    # CALCULATE 1st PRODUCT
    for nums in productNums:
        totalProduct *= nums
    positiveProducts.append(totalProduct)

    # FORM PRODUCT 2
    productNums = []
    totalProduct = 1
    end = -1
    for index in range(0, len(lambdaChoices)):
        '''
            from chosen lambdas 1, 3, 4, 5
            create 4 differences:
            # (1-4)(4-3)(3-5)(5-1)
            (0-2)(1-3)(2-1)(3-0)
        '''
        if index == 0 or index == 1:
            diff = int(lambdaChoices[index]) - int(lambdaChoices[index + 2])
        else:
            diff = int(lambdaChoices[index]) - int(lambdaChoices[index + end])
            end -= 2
        productNums.append(diff)
    # CALCULATE 2nd PRODUCT
    for nums in productNums:
        totalProduct *= nums
    positiveProducts.append(totalProduct)

    # FORM PRODUCT 3
    productNums = []
    totalProduct = 1
    offset = 2
    end = 1
    for index in range(0, len(lambdaChoices)):
        '''
            from chosen lambdas 1, 3, 4, 5
            create 4 differences:
            # (1-4)(4-5)(5-3)(3-1)
            (0-2)(1-0)(2-3)(3-1)
        '''
        if index == 0 or index == 1:
            diff = int(lambdaChoices[index]) - int(lambdaChoices[index + offset])
            offset = -1
        else:
            diff = int(lambdaChoices[index]) - int(lambdaChoices[index + end])
            end = -2
        productNums.append(diff)
    # CALCULATE 3rd PRODUCT
    for nums in productNums:
        totalProduct *= nums
    positiveProducts.append(totalProduct)

    # REMOVE NEGATIVE PRODUCT
    for product in positiveProducts:
        if product * -1 > 0:
            positiveProducts.remove(product)
    # RETURN ONLY POSITIVE PRODUCTS
    return positiveProducts

for set in integerSets:
    print(formPositiveProducts(chooseFour(set)))
    break

test = [1, 33, 36, 43]
posProducts = formPositiveProducts(test)
# FACTORIZE EACH PRODUCT
print(posProducts)