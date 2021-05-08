import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def getNewDistribution(data):
    total = sum(data)
    updatedDistribution = []
    for i in range(len(data)):
        updatedDistribution.append(float(data[i] / total))
    return updatedDistribution

if __name__ == "__main__":
    random.seed(time.time())
    np.random.seed(42)
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

    iterations = int(input("Enter number of iterations: "))

    track = []
    deviationTemp = [[] for _ in range(numOfClasses)]
    for loop in range(iterations):
        copyData = data.copy()
        population = list(range(0, numOfClasses))
        newDistribution = initialDistribution.copy()
        for i in range(removeNum):
            nonZeroIndices = [x for x in list(range(0, len(copyData))) if copyData[x] != 0]
            nonZeroPopulation = [population[x] for x in nonZeroIndices]
            nonZeroDistribution = [newDistribution[x] for x in nonZeroIndices]
            randChoice = random.choices(nonZeroPopulation, nonZeroDistribution)
            copyData[randChoice[0]] -= 1
            newDistribution = getNewDistribution(copyData)
        track.append(newDistribution)
        independentDeviations = []

        for j in range(len(initialDistribution)):
            #currDeviation = abs(newDistribution[j] - initialDistribution[j]) / initialDistribution[j]
            #currDeviation = (newDistribution[j] - initialDistribution[j]) / initialDistribution[j]
            #currDeviation *= 100.0
            #deviationTemp[j].append(currDeviation)
            deviationTemp[j].append(newDistribution[j])

    #print("Final Distribution: ", newDistribution)
    #print(data)
    #deviation.sort()
    #print(deviation)
    #plt.hist(deviation, bins='auto')
    #plt.show()
    #for i in range(len(deviationTemp)):
    #    plt.hist(deviationTemp[i], bins='auto')
    #plt.show()
    from scipy.stats import norm
    fig, axs = plt.subplots(len(deviationTemp))
    for i in range(len(deviationTemp)):
        axs[i].hist(deviationTemp[i], bins=10, density=True)
        #xmin, xmax = axs[i].xlim()
        #print(xmin, " ", xmax)
        mu, std = norm.fit(deviationTemp[i])
        x = np.linspace(norm.ppf(0.44, loc = mu, scale = 1), norm.ppf(0.55, loc = mu), 100)
        p = norm.pdf(x, mu, std)
        axs[i].plot(x, p, 'k', linewidth=2)
    plt.show()


