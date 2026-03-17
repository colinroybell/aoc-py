import pytest
from ecst02.day03 import Run_st02_03


class Test_st02_03:
    def setup_class(self):
        self.day = Run_st02_03()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1", trace="part1_trace1", roll_test=True)

    def test_bringup_1_2(self):
        assert self.day.run_part("1", "test2", trace="part1_trace2") == 844

    def test_bringup_2(self):
        assert self.day.run_part("2", "test3") == "1,3,4,2"

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test4") == 33

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test5") == 1125

    def test_regression_1(self):
        assert self.day.run_part("1") == 633

    def test_regression_2(self):
        assert self.day.run_part("2") == "4,7,9,8,1,5,3,2,6"

    def test_regression_3(self):
        assert self.day.run_part("3") == 154065
