import pytest
from aoc2023.day20 import Run_2023_20


class Test_2023_20:
    def setup_class(self):
        self.day = Run_2023_20()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 32000000

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 11687500

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 898731036

    def test_regression_b(self):
        assert self.day.run_part("b") == 229414480926893
