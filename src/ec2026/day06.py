from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2026_06(DayBase):
    YEAR = "2026"
    DAY = "06"
    PREFIX = "ec"


def find_ingredients_used(recipes, start):
    ingredients_used = set()
    ingredient_queue = [start]

    while ingredient_queue:
        item = ingredient_queue.pop()
        if item in ingredients_used:
            continue
        ingredients_used.add(item)
        if item in recipes:
            for i in recipes[item]:
                ingredient_queue.append(i)
    return ingredients_used


def part_1(input, part=1):
    generator = input_generator(input)
    recipes = {}
    counts = {}
    for line in generator:
        fields = line.split(":")
        ingredients = fields[1].split(",")
        if part == 1:
            recipes[fields[0]] = ingredients
        else:
            for i in ingredients:
                if i not in recipes:
                    recipes[i] = [fields[0]]
                else:
                    recipes[i].append(fields[0])
        if part == 3:
            counts[fields[0]] = 0

    if part < 3:
        ingredients_used = find_ingredients_used(recipes, "NULL")

        return len(ingredients_used) - 1
    else:
        for round in range(1, 4):
            start = f"NULLv{round}"
            ingredients_used = find_ingredients_used(recipes, start)
            for i in ingredients_used:
                if i != start:
                    counts[i] += 1

        used = 0
        for _, v in counts.items():
            if v >= 2:
                used += 1
        return used


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2026_06().run_cmdline()
