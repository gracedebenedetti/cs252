'''
attractions.py by Grace de Benedetti
Algorithms Spring 2021
HW 07
'''

import sys

def minimize(destinations, k):
    attractions = [line.strip().lower() for line in open(destinations)]
    destinationWeights = []
    #get destination weights from file
    for attraction in attractions:
        cost = int(attraction[2:])
        destinationWeights.append(cost)
    numberDests = len(destinationWeights)
    destinationWeights.append(0)

    #create matrix
    costMatrix = [[0 for i in range (numberDests + 2)] for j in range (k+ 1)]

    #fill in matrix with cheapest values
    for numberSkipped in range(0, k + 1):
        for destinationIndex in range(0, numberDests + 2):
            if destinationIndex == 0:
                costMatrix[numberSkipped][destinationIndex] = 0
            elif numberSkipped == 0 and destinationIndex >= 1:
                costMatrix[numberSkipped][destinationIndex] = costMatrix[numberSkipped][destinationIndex-1] + destinationWeights[destinationIndex-1]
            else:
                costMatrix[numberSkipped][destinationIndex] = min(costMatrix[numberSkipped-1][destinationIndex-2], costMatrix[numberSkipped][destinationIndex-1]) + destinationWeights[destinationIndex-1]
    #find minimum cost
    minCost = costMatrix[k] [(numberDests + 1)]

    #find skipped attractions
    skippedAttractions = ''
    #start at last square in matrix
    numberSkipped = k
    destinationIndex = numberDests + 1

    #trace back to first square
    while destinationIndex != 0 and numberSkipped != 0:
        if costMatrix[numberSkipped-1][destinationIndex-2] < costMatrix[numberSkipped][destinationIndex-1]:
            skippedAttractions =  attractions[destinationIndex-2][0] + ' ' + skippedAttractions
            numberSkipped = numberSkipped-1
            destinationIndex = destinationIndex-2
        else:
            destinationIndex = destinationIndex-1
    #output values
    print(skippedAttractions)
    print(minCost)

def main():
    filename = sys.argv[1]
    k = int(sys.argv[2])
    minimize(filename, k)

if __name__ == '__main__':
    main()
