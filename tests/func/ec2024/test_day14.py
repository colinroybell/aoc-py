import pytest
from ec2024.day14 import Run_2024_14


class Test_2024_14:
    def setup_class(self):
        self.day = Run_2024_14()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 7

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 32

    def test_bringup_3(self):
        assert self.day.run_part("3", "test2") == 5

    def test_regression_1(self):
        assert self.day.run_part("1") == 157

    def test_regression_2(self):
        assert self.day.run_part("2") == 4988

    def test_regression_3(self):
        assert self.day.run_part("3") == 1604
