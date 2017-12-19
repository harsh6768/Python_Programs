# create a graph having verteces and
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ',' + str(self.value) + ',' + str(self.weight) + '>'
        return result


def value(item):
    return item.getValue()


def weightInverse(item):
    return 1.0 / item.getWeight()


def density(item):
    return item.getValue() / item.getWeight()


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items


# greedy Algrithm

def greedy(items, maxWeight, keyFunction):
    itemscopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalvalue = 0.0
    totalweight = 0.0
    for i in range(len(itemscopy)):
        if (totalweight + itemscopy[i].getWeight()) <= maxWeight:
            result.append(itemscopy[i])
            totalweight += itemscopy[i].getWeight()
            totalvalue += itemscopy[i].getValue()
    return (result, totalvalue)


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print("TOTAL VALUE OF ITEMS TAKEN = ", val)
    for items in taken:
        print(' ', items)

 
def testGreedys(a):
    maxweight = a
    items = buildItems()
    print('USE GREEDY BY VALUE to FILL knapsack of size', maxweight)
    testGreedy(items, maxweight, value)
    print('USE GREEDY BY WEIGHT to FILL knapsack of size', maxweight)
    testGreedy(items, maxweight, weightInverse)
    print('USE GREEDY BY DENSITY to FILL knapsack of size', maxweight)
    testGreedy(items, maxweight, density)


testGreedys(30)
