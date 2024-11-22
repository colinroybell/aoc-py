import pytest
from ec2024.day11 import Run_2024_11


class Test_2024_11:
    def setup_class(self):
        self.day = Run_2024_11()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 8

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 268815

    def test_regression_1(self):
        assert self.day.run_part("1") == 33

    def test_regression_2(self):
        assert self.day.run_part("2") == 255223

    def test_regression_3(self):
        assert self.day.run_part("3") == 1158251066200
