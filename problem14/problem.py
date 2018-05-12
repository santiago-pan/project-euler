# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

def isEven(number):
    return number % 2 is 0

def getNextNumber(number):
    if(isEven(number)):
        return number/2
    else:
        return (number*3) + 1

def generateSeries(number):
    numOfTerms = 1
    while (number != 1):
        number = getNextNumber(number)
        numOfTerms = numOfTerms + 1
    return numOfTerms

def findLongestSerie(maxNumber):
    maxChain = 1
    maxChainNumber = 1
    for number in range(2, maxNumber + 1):
        currentChain = generateSeries(number)
        if currentChain > maxChain:
            maxChain = currentChain
            maxChainNumber = number

    return maxChainNumber

