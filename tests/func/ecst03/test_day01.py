import pytest
from ecst03.day01 import Run_st03_01


class Test_st03_01:
    def setup_class(self):
        self.day = Run_st03_01()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 9166

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 2456

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 292320

    def test_regression_1(self):
        assert self.day.run_part("1") == 46129

    def test_regression_2(self):
        assert self.day.run_part("2") == 77264

    def test_regression_3(self):
        assert self.day.run_part("3") == 10358287
