import pytest
from ec2024.day01 import Run_2024_01


class Test_2024_01:
    def setup_class(self):
        self.day = Run_2024_01()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 5

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 28

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 30

    def test_regression_1(self):
        assert self.day.run_part("1") == 1324

    def test_regression_2(self):
        assert self.day.run_part("2") == 5666

    def test_regression_3(self):
        assert self.day.run_part("3") == 27834
