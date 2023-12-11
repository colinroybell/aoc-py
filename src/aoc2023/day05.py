from utils.day_base import DayBase
from utils.data_input import input_generator

class Run_2023_05(DayBase):
    YEAR='2023'
    DAY='05'

class Map:
    def __init__(self):
        self.map = []

    def add_mapping(self, dest, source, length):
        self.map.append((dest, source, length))

    def do_map(self, value):
        for mapping in self.map:
            diff = value - mapping[1]
            if 0<= diff < mapping[2]:
                print(mapping,value,diff)
                return diff + mapping[0]
        return value

    def do_map_range(self, start, length):
        length_no_map = length
        for mapping in self.map:
            diff_next = mapping[1] - start
            if diff_next > 0 and diff_next < length_no_map:
                length_no_map = diff_next
            diff = start - mapping[1]
            if 0 <= diff < mapping[2]:
                if diff + length > mapping[2]:
                    length = mapping[2] - diff
                return (diff + mapping[0], length)
        return (start, length_no_map)

def mapping_recurse(maps, start, length):
    maps_next = maps[1:]
    minimum = None
    while length > 0:
        (value, map_length) = maps[0].do_map_range(start, length)
        start += map_length
        length -= map_length
        if maps_next:
            value = mapping_recurse(maps_next, value, map_length)
        if minimum == None or value < minimum:
            minimum = value
    return minimum

def part_a(input, part_b = False):
    part_a = not part_b
    maps = []
    seeds = []
    generator = input_generator(input)
    seed_strings = next(generator)[7:].split(' ')
    for s in seed_strings:
        seeds.append(int(s))

    _ = next(generator)

    done = False
    while not done:
        line = next(generator, None)

        print('map', line)
        map = Map()
        maps.append(map)
        while 1:
            line = next(generator, None)
            if line == None:
                done = True
                break
            if line == '':
                break
            nums = [int(x) for x in line.split(' ')]
            print(line, nums)
            map.add_mapping(nums[0], nums[1], nums[2])
    minimum = None
    if part_a:

        for s in seeds:
            value = s
            print('start', value)
            for m in maps:
                value = m.do_map(value)
                print(value)
            if minimum == None or value < minimum:
                minimum = value
        return minimum
    else:
        while len(seeds):
            start = seeds[0]
            length = seeds[1]
            seeds = seeds[2:]
            value = mapping_recurse(maps, start, length)
            if minimum == None or value < minimum:
                minimum = value
        return minimum


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_05().run_cmdline()
