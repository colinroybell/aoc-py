import pytest
from ec2024.day03 import Run_2024_03


class Test_2024_03:
    def setup_class(self):
        self.day = Run_2024_03()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 35

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 29

    def test_regression_1(self):
        assert self.day.run_part("1") == 128

    def test_regression_2(self):
        assert self.day.run_part("2") == 2618

    def test_regression_3(self):
        assert self.day.run_part("3") == 9860
