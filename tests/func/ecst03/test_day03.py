import pytest
from ecst03.day03 import Run_st03_03


class Test_st03_03:
    def setup_class(self):
        self.day = Run_st03_03()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 43

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 50

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 38

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test4") == 60

    def test_regression_1(self):
        assert self.day.run_part("1") == 6269

    def test_regression_2(self):
        assert self.day.run_part("2") == 321138

    def test_regression_3(self):
        assert self.day.run_part("3") == 389641
