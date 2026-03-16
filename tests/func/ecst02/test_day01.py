import pytest
from ecst02.day01 import Run_st02_01


class Test_st02_01:
    def setup_class(self):
        self.day = Run_st02_01()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1") == 3

    def test_bringup_1_2(self):
        assert self.day.run_part("1", "test2", trace="part1_trace1") == 26

    def test_bringup_2(self):
        assert self.day.run_part("2", "test3", trace="part2_trace1") == 115

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test4") == "13 43"

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test5") == "25 66"

    def test_bringup_3_3(self):
        assert self.day.run_part("3", "test6") == "39 122"

    def test_regression_1(self):
        assert self.day.run_part("1") == 48

    def test_regression_2(self):
        assert self.day.run_part("2") == 1136

    def test_regression_3(self):
        assert self.day.run_part("3") == "37 109"
