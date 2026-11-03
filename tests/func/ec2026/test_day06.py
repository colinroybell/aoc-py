import pytest
from ec2026.day06 import Run_2026_06


class Test_2026_06:
    def setup_class(self):
        self.day = Run_2026_06()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 7

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 6

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 3

    def test_regression_1(self):
        assert self.day.run_part("1") == 41

    def test_regression_2(self):
        assert self.day.run_part("2") == 855

    def test_regression_3(self):
        assert self.day.run_part("3") == 1653
