import pytest
from ec2024.day17 import Run_2024_17


class Test_2024_17:
    def setup_class(self):
        self.day = Run_2024_17()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 16

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 15624

    def test_regression_1(self):
        assert self.day.run_part("1") == 140

    def test_regression_2(self):
        assert self.day.run_part("2") == 1191

    def test_regression_3(self):
        assert self.day.run_part("3") == 4858178832
