import pytest
from ec2024.day18 import Run_2024_18


class Test_2024_18:
    def setup_class(self):
        self.day = Run_2024_18()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 11

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 21

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 12

    def test_regression_1(self):
        assert self.day.run_part("1") == 105

    def test_regression_2(self):
        assert self.day.run_part("2") == 1341

    def test_regression_3(self):
        assert self.day.run_part("3") == 293297
