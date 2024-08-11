from random import randint
from itertools import combinations
from pprint import pprint
import numpy as np

def readSetsOutput():
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
    return integerSets

def formatForFile(sets, file):
    for set in sets:
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

def chooseFour(set):
    '''OLD IMPLEMENTATION w/ RANDOM
    lambdaIndices = []
    while len(lambdaIndices) < 4:
        index = randint(0, len(set) - 1)
        if index not in lambdaIndices:
            lambdaIndices.append(index)
            lambdaIndices.sort()
    lambdaChoices = []
    for index in range(0, len(lambdaIndices)):
        lambdaChoices.append(set[lambdaIndices[index]])
    return lambdaChoices'''
    fourCombinations = list(combinations(set, 4))
    return fourCombinations


def formPositiveProducts(fourLambdas):
    allProducts = []
    for lambdaChoices in fourLambdas:
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
        allProducts.append(positiveProducts)
    return allProducts

def onlyOddPrimeFactors(positiveProducts):
    onlyOdds = []
    for products in positiveProducts:
        primeFactors = []
        # FACTORIZE EACH PRODUCT
        for product in products:
            primes = []
            for num in range(2, 18):
                count = 0
                if product % num == 0:
                    while product % num == 0:
                        product /= num
                        count += 1
                    if product == 1:
                        break
                if count % 2 == 1:
                    primes.append(num)
            if count % 2 == 1:
                primes.append(num)
            if len(primes) == 0:
                primeFactors.append(None)
            else:
                primeFactors.append(primes)
        onlyOdds.append(primeFactors)
    return onlyOdds

def calculateScore(onlyOdds):
    # currently cannot calculate score, cant figure out how to change
    # items in pairs to all combinations of [-1, 1].
    '''EXAMPLE
        list = [[3, 7], [3, 17]]
        let 3 be -1
        let 7 be 1
        let 17 be 1
        list is now = [[-1, 1], [-1, 1]]
        
        # Scoring implementation below.
        totalScore = 2
        for pair in list:
            currentScore = 1
            for index in range(0, len(pair))
                currentScore *= pair[index]
            totalScore += currentScore
    '''
    scoreChoices = [1, -1]
    for list in onlyOdds:
        overallScore = 2
        # write all valid exponents to single list.
        for pair in list:
            score = 1
            if pair == None:
                continue
            print(pair)
        break            

def main():
    sidonSets = readSetsOutput()
    file = open("primeFactors.txt", 'w')

    file.write("This file is for testing the implemtation of:")
    file.write("\nForming 4 Lambda Choices, Forming Positive Products, Taking only Odd Exponent Prime Factors.")
    testSet = ['1', '35', '161', '170', '251', '545']
    file.write("\n\nTesting Set: ")
    file.write(str(testSet))
    file.write("\n\nNow testing all (chooseFour) combinations of four lambda choices.\n")
    formatForFile(chooseFour(testSet), file)
    file.write("\nNow testing (formPositiveProducts) positive products from lambda choices.\n")
    formatForFile(formPositiveProducts(chooseFour(testSet)), file)
    file.write("\nNow testing (onlyOddPrimeFactors) displaying only Odd Exponent Prime Factors.\n")
    formatForFile(onlyOddPrimeFactors(formPositiveProducts(chooseFour(testSet))), file)

    calculateScore(onlyOddPrimeFactors(formPositiveProducts(chooseFour(testSet))))

    '''print("Test set: ['1', '35', '161', '170', '251', '545']")
    print("Choose Four: ", chooseFour(['1', '35', '161', '170', '251', '545']))
    print("Positive Products: ", formPositiveProducts(chooseFour(['1', '35', '161', '170', '251', '545'])))
    print("\nOnly Odd Prime Factors: ", onlyOddPrimeFactors(formPositiveProducts(chooseFour(['1', '35', '161', '170', '251', '545']))))'''
main()