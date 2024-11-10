import pytest
from ec2024.day04 import Run_2024_04


class Test_2024_04:
    def setup_class(self):
        self.day = Run_2024_04()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 10

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 8

    def test_regression_1(self):
        assert self.day.run_part("1") == 81

    def test_regression_2(self):
        assert self.day.run_part("2") == 953804

    def test_regression_3(self):
        assert self.day.run_part("3") == 126084734
