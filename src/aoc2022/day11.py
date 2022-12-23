from utils.day_base import DayBase
from utils.data_input import input_generator
import re
import math


class Run_2022_11(DayBase):
    YEAR = "2022"
    DAY = "11"


def part_a(input, part_b=False):
    part_a = not part_b
    monkey_re = re.compile(r"Monkey (\d+):")
    starting_re = re.compile(r": (.+)")
    operation_re = re.compile(r"new = (.+)")
    divisible_re = re.compile(r"by (\d+)")
    throw_re = re.compile(r"(\d+)")
    generator = input_generator(input)

    monkeys = []
    while 1:
        line = next(generator)
        m = monkey_re.match(line)
        assert m
        id = int(m.group(1))
        monkey = {}
        monkeys.append(monkey)
        monkey["id"] = id
        monkey["count"] = 0

        line = next(generator)
        m = starting_re.search(line)
        assert m
        items = m.group(1).split(",")
        print(items)
        monkey["items"] = [int(item) for item in items]

        line = next(generator)
        m = operation_re.search(line)
        assert m
        monkey["operation"] = m.group(1)

        line = next(generator)
        m = divisible_re.search(line)
        assert m
        monkey["divisible"] = int(m.group(1))

        line = next(generator)
        m = throw_re.search(line)
        assert m
        monkey["true"] = int(m.group(1))

        line = next(generator)
        m = throw_re.search(line)
        assert m
        monkey["false"] = int(m.group(1))

        line = next(generator, None)
        if line == None:
            break

    if part_a:
        round_limit = 20 + 1
    else:
        round_limit = 10000 + 1

    # Reduce numbers for speed. (lcm quicker than just product)
    modulo = math.prod([monkey["divisible"] for monkey in monkeys])

    for round in range(1, round_limit):
        # print("Round ",round)
        for monkey in monkeys:
            # print("Monkey ",monkey['id'])
            for item in monkey["items"]:
                monkey["count"] += 1
                old = item
                op = eval(monkey["operation"])
                if part_a:
                    d3 = op // 3
                else:
                    d3 = op % modulo
                # print(old," to ",op," to ",d3)
                if d3 % monkey["divisible"] == 0:
                    new_monkey = monkey["true"]
                else:
                    new_monkey = monkey["false"]
                # print("to monkey ",new_monkey)
                monkeys[new_monkey]["items"].append(d3)
            monkey["items"] = []
    counts = [monkey["count"] for monkey in monkeys]
    counts.sort(reverse=True)
    return counts[0] * counts[1]


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2022_11().run_cmdline()
