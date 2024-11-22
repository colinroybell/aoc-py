import pytest
from ec2024.day12 import Run_2024_12


class Test_2024_12:
    def setup_class(self):
        self.day = Run_2024_12()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 13

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 22

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 11

    def test_bringup_3_2(self):
        assert self.day.run_part("3", ["5 5"]) == 2

    def test_regression_1(self):
        assert self.day.run_part("1") == 218

    def test_regression_2(self):
        assert self.day.run_part("2") == 20357

    def test_regression_3(self):
        assert self.day.run_part("3") == 749435
