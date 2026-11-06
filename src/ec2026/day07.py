from utils.day_base import DayBase
from utils.data_input import input_generator
import copy


class Run_2026_07(DayBase):
    YEAR = "2026"
    DAY = "07"
    PREFIX = "ec"


def parse_fields(line):
    strings = line.split(", ")
    fields = {}
    for string in strings:
        id, value = string.split("=")
        if id == "connections":
            value = [int(s) for s in value.split(",")]
        else:
            value = int(value)
        fields[id] = value
    return fields


def forward_impulse(clouds, dead_clouds, next_impulses, id, strength, v):
    for out_id in clouds[id]["connections"]:
        if out_id in dead_clouds:
            continue
        impulse = (out_id, strength)
        if impulse not in next_impulses:
            next_impulses[impulse] = v
        else:
            next_impulses[impulse] += v


def score(clouds, id, strength, explosion_limit=None):
    impulses = {(id, strength): 1}
    dead_clouds = set()
    while impulses:
        next_impulses = {}
        for (id, strength), v in impulses.items():
            if id in dead_clouds:
                continue
            clouds[id]["energy"] += strength * v
            if strength > 1:
                forward_impulse(clouds, dead_clouds, next_impulses, id, strength - 1, v)

        if explosion_limit:
            for id in clouds:
                if id not in dead_clouds and clouds[id]["energy"] >= explosion_limit:
                    dead_clouds.add(id)
                    clouds[id]["energy"] = 0
                    forward_impulse(clouds, dead_clouds, next_impulses, id, 10, 1)

        impulses = next_impulses

    total = sum(clouds[id]["energy"] for id in clouds)
    return total


def part_1(input, part=1, explosion_limit=None):
    generator = input_generator(input)
    clouds = {}
    best_cloud = None
    best_length = 0
    for line in generator:
        fields = parse_fields(line)
        id = fields["id"]
        clouds[id] = fields
        connections = clouds[id]
        length = len(clouds[id]["connections"])
        if length > best_length:
            best_length = length
            best_cloud = id
    if part < 3:
        if part == 1:
            strength = 5
        else:
            strength = 10

        return score(clouds, best_cloud, strength)
    else:
        best_s = 0
        for id in clouds:
            s = score(copy.deepcopy(clouds), id, 10, explosion_limit)
            if s > best_s:
                best_s = s
        return best_s


def part_2(input):
    return part_1(input, part=2)


def part_3(input, explosion_limit=1000000):
    return part_1(input, part=3, explosion_limit=explosion_limit)


if __name__ == "__main__":
    Run_2026_07().run_cmdline()
