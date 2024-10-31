from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_15(DayBase):
    YEAR = "2015"
    DAY = "15"


def recurse(attrs, count, counts, score_left, part_b):
    if count == len(attrs) - 1:
        counts.append(score_left)
        prod = 1
        amounts = []
        for i in range(5):
            amount = 0

            for j in range(len(attrs)):
                amount += counts[j] * attrs[j][i]
            if amount < 0:
                amount = 0
            if i == 4:
                print(amount, part_b)
                if not part_b or part_b and amount == 500:
                    amount = 1
                else:
                    amount = 0
            prod *= amount
            amounts.append(amount)
        print(counts, amounts, prod)
        return prod
    else:
        best = 0
        for s in range(score_left + 1):
            new_counts = counts.copy()
            new_counts.append(s)
            prod = recurse(attrs, count + 1, new_counts, score_left - s, part_b)
            best = max(best, prod)
        return best


def part_a(input, part_b=False):
    attrs = []
    for line in input_generator(input):
        f1 = line.split(":")
        f2 = f1[1].split(",")
        attr_line = []
        for i in range(5):
            f3 = f2[i].split(" ")
            print(f3)
            attr_line.append(int(f3[2]))
        attrs.append(attr_line)
    print(attrs)

    return recurse(attrs, 0, [], 100, part_b)


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2015_15().run_cmdline()
