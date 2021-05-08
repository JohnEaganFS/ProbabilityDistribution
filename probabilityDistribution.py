import random
import time

def getNewDistribution(data):
    total = sum(data)
    updatedDistribution = []
    for i in range(len(data)):
        updatedDistribution.append(data[i] / total)
    return updatedDistribution

if __name__ == "__main__":
    random.seed(time.time())
    dataSize = int(input("Enter amount of data instances: "))
    numOfClasses = int(input("Enter number of different classes: "))
    initialDistribution = []
    for i in range(numOfClasses):
        inputDist = (float(input("Enter distribution (input 0.3 -> 30%) for class " + str(i + 1) + ":")))
        initialDistribution.append(inputDist)

    if sum(initialDistribution) > 1.0 or sum(initialDistribution) < 1.0:
        raise Exception("That don't add up to 1.0. ლ(~•̀︿•́~)つ︻̷┻̿═━一")

    removeNum = int(input("Enter amount of instances that should be removed: "))
    if removeNum >= dataSize:
        raise Exception("You can't do that. Data is important. ∩༼˵☯‿☯˵༽つ¤=[]:::::>")

    data = []
    for i in range(numOfClasses):
        data.append(int(initialDistribution[i] * dataSize))

    population = list(range(0, numOfClasses))
    newDistribution = initialDistribution
    for i in range(removeNum):
        nonZeroIndices = [x for x in list(range(0, len(data))) if data[x] != 0]
        nonZeroPopulation = [population[x] for x in nonZeroIndices]
        nonZeroDistribution = [newDistribution[x] for x in nonZeroIndices]
        randChoice = random.choices(nonZeroPopulation, newDistribution)
        data[randChoice[0]] -= 1
        newDistribution = getNewDistribution(data)

    print("Final Distribution: ", newDistribution)
    print(data)

    import matplotlib.pyplot as plt


