from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2020_21(DayBase):
    YEAR = "2020"
    DAY = "21"


def part_a(input):
    foods = []
    ingredients = set()
    allergens = set()
    split_re = re.compile(r"(.+) \(contains (.+)\)")

    for line in input_generator(input):
        m = split_re.match(line)
        assert m
        ing_items = m.group(1).split(" ")
        for ing in ing_items:
            ingredients.add(ing)
        all_items = m.group(2).split(", ")
        for all in all_items:
            allergens.add(all)
        foods.append((ing_items, all_items))

    safe = ingredients
    for all in allergens:
        first = True
        for food in foods:
            if all in food[1]:
                if first:
                    candidates = set(food[0])
                    first = False
                else:
                    candidates &= set(food[0])
        for ing in candidates:
            if ing in safe:
                safe.remove(ing)

    count = 0
    for ing in safe:
        for food in foods:
            if ing in food[0]:
                count += 1
    return count


def part_b(input):
    foods = []
    ingredients = set()
    allergens = set()
    split_re = re.compile(r"(.+) \(contains (.+)\)")
    for line in input_generator(input):
        m = split_re.match(line)
        assert m
        ing_items = m.group(1).split(" ")
        print(ing_items)
        for ing in ing_items:
            ingredients.add(ing)
        all_items = m.group(2).split(", ")
        for all in all_items:
            allergens.add(all)
        foods.append((ing_items, all_items))

    cand_ing = {}
    cand_all = {}
    for all in allergens:
        first = True
        for food in foods:
            if all in food[1]:
                if first:
                    candidates = set(food[0])
                    first = False
                else:
                    candidates &= set(food[0])
        cand_ing[all] = candidates
        for ing in candidates:
            if ing not in cand_all:
                cand_all[ing] = set()
            cand_all[ing].add(all)

    change = True

    while change:
        change = False
        for all, items in cand_ing.items():
            if len(items) == 1:
                ing = list(items)[0]
                for other_all in cand_all[ing]:
                    if all == other_all:
                        continue
                    cand_ing[other_all].remove(ing)
                    change = True
                cand_all[ing] = set([all])

        for ing, items in cand_all.items():
            if len(items) == 1:
                all = list(items)[0]
                for other_ing in cand_ing[all]:
                    if ing == other_ing:
                        continue
                    cand_all[other_ing].remove(all)
                    change = True
                cand_ing[all] = set([ing])

    all_list = sorted(cand_ing.keys())
    text = ""
    for all in all_list:
        text += list(cand_ing[all])[0]
        text += ","

    text = text[:-1]
    return text


if __name__ == "__main__":
    Run_2020_21().run_cmdline()
