import pytest
from ecst01.day03 import Run_st01_03


class Test_st01_03:
    def setup_class(self):
        self.day = Run_st01_03()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 1310

    def test_bringup_2_1(self):
        assert self.day.run_part("2", "test2") == 14

    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test3") == 13659

    # Part 3 is just a rerun

    def test_regression_1(self):
        assert self.day.run_part("1") == 3537

    def test_regression_2(self):
        assert self.day.run_part("2") == 1019086

    def test_regression_3(self):
        assert self.day.run_part("3") == 99537710915
