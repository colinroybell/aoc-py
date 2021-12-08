import pytest
from aoc2021.day08 import Run_2021_08


class Test_2021_08:
    def setup_class(self):
        self.day = Run_2021_08()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 26

    def test_bringup_b(self):
        assert (
            self.day.run_part(
                "b",
                [
                    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |",
                    "cdfeb fcadb cdfeb cdbaf",
                ],
            )
            == 5353
        )
        assert self.day.run_part("b", "test1") == 61229

    def test_regression_a(self):
        assert self.day.run_part("a") == 416

    def test_regression_b(self):
        assert self.day.run_part("b") == 1043697
