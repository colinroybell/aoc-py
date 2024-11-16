import pytest
from ec2024.day08 import Run_2024_08


class Test_2024_08:
    def setup_class(self):
        self.day = Run_2024_08()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 21

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 27

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 2

    def test_regression_1(self):
        assert self.day.run_part("1") == 11891913

    def test_regression_2(self):
        assert self.day.run_part("2") == 125757249

    def test_regression_3(self):
        assert self.day.run_part("3") == 41082
