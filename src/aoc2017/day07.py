from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_07(DayBase):
    YEAR = "2017"
    DAY = "07"


parent = {}
children = {}
weight = {}
totalWeight = {}
words = []

# TODO: this doesn't work if the odd one comes first. (True of the test data, but real data does work.)
def computeTotalWeights(disc):
    totalWeight[disc] = weight[disc]
    targetWeight = 0
    first = 1
    for child in children[disc]:
        (answer, childWeight) = computeTotalWeights(child)
        if answer:
            return (True, childWeight)
        if first:
            targetWeight = childWeight
            first = 0
            firstChild = child
        else:
            if childWeight != targetWeight:
                print(
                    "{} says: Want {} to be {} but it is {}. Base weight {}. First child {}, weight {}".format(
                        disc,
                        child,
                        targetWeight,
                        childWeight,
                        weight[child],
                        firstChild,
                        weight[firstChild],
                    )
                )
                revisedWeight = weight[child] + targetWeight - childWeight
                return (True, revisedWeight)
        totalWeight[disc] += childWeight
    print(disc, totalWeight[disc])
    return (False, totalWeight[disc])


def part_a(input, part_b=False):
    part_a = not part_b

    countP = 0
    countW = 0
    for line in input_generator(input):
        countW += 1
        array = line.split(" ")

        word = array[0]
        # print(array[1])
        weight[word] = int(array[1][1:-1])
        children[word] = []
        words.append(word)
        for i in range(3, len(array)):
            child = array[i]
            if child[-1] == ",":
                child = child[:-1]
            parent[child] = word
            children[word].append(child)
            # print("{} -> {}".format(child,word))
            countP += 1

    for word in words:
        if word not in parent:
            base = word
    if part_a:
        return base
    else:
        return computeTotalWeights(base)[1]


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_07().run_cmdline()
