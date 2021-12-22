import pytest
from aoc2021.day22 import Run_2021_22


class Test_2021_22:
    def setup_class(self):
        self.day = Run_2021_22()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 39

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 590784

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 39

    def test_bringup_b_2(self):
        # Test 4 is test 2 with the last two (out of bounds) lines removed
        assert self.day.run_part("b", "test4") == 590784

    def test_bringup_b_3(self):
        assert self.day.run_part("b", "test3") == 2758514936282235

    def test_bringup_b_5(self):
        assert self.day.run_part("b", "test5") == 55 * 47 * 46

    def test_regression_a(self):
        assert self.day.run_part("a") == 542711

    def test_regression_b(self):
        assert self.day.run_part("b") == 1160303042684776
