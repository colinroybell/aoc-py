import importlib
import sys
from abc import ABC, abstractmethod


class DayBase:
    YEAR = ""
    DAY = ""
    PART_AS_SUFFIX = False

    def run_part(self, part, input=None, **kwargs):
        aoc_module = importlib.import_module("aoc{}.day{}".format(self.YEAR, self.DAY))
        if not isinstance(input, list):
            input = self.input_filename(part, input)
        if part == "a":
            return aoc_module.part_a(input, **kwargs)
        elif part == "b":
            return aoc_module.part_b(input, **kwargs)
        else:
            assert False
            return 0

    def input_filename(self, part, suffix):
        #suffix = "test1"
        if suffix:
            suffix = "_" + suffix
        else:
            suffix = ""
        if self.PART_AS_SUFFIX:
            suffix = "part" + suffix
        return "data/aoc{}/day{}{}.txt".format(self.YEAR, self.DAY, suffix)

    def run_cmdline(self):

        if "a" in sys.argv:
            part = "a"
        elif "b" in sys.argv:
            part = "b"
        else:
            assert "Part not a or b"
        print(self.run_part(part))
