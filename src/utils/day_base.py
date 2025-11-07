import importlib
import sys
from abc import ABC, abstractmethod


class DayBase:
    YEAR = ""
    DAY = ""
    PREFIX = "aoc"
    PART_AS_SUFFIX = False

    def run_part(self, part, input=None, **kwargs):
        aoc_module = importlib.import_module(
            "{}{}.day{}".format(self.PREFIX, self.YEAR, self.DAY)
        )
        if part.isnumeric():
            aoc_module.PART = int(part)
        else:
            aoc_module.PART = part

        if not isinstance(input, list):
            input = self.input_filename(part, input)

        if part == "a":
            return aoc_module.part_a(input, **kwargs)
        elif part == "b":
            return aoc_module.part_b(input, **kwargs)
        elif part == "1":
            return aoc_module.part_1(input, **kwargs)
        elif part == "2":
            return aoc_module.part_2(input, **kwargs)
        elif part == "3":
            return aoc_module.part_3(input, **kwargs)
        else:
            assert False
            return 0

    def input_filename(self, part, suffix):
        if suffix:
            suffix = "_" + suffix
        else:
            if self.PREFIX == "ec":
                if self.YEAR == "2024":
                    suffix = "_part_" + part
                else:
                    suffix = "_part" + part
            else:
                suffix = ""
        if self.PART_AS_SUFFIX:
            suffix = "part" + suffix
        return "data/{}{}/day{}{}.txt".format(self.PREFIX, self.YEAR, self.DAY, suffix)

    def run_cmdline(self):
        print(sys.argv)
        part = sys.argv[1]
        suffix = None
        if len(sys.argv) > 2:
            suffix = sys.argv[2]
        print(self.run_part(part, suffix))
