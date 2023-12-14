import pytest
from aoc2023.day15 import Run_2023_15, hash


class Test_2023_15:
    def setup_class(self):
        self.day = Run_2023_15()

    def test_bringup_hash(self):
        assert hash("HASH") == 52

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 1320

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 145

    def test_regression_a(self):
        assert self.day.run_part("a") == 514639

    def test_regression_b(self):
        assert self.day.run_part("b") == 279470
