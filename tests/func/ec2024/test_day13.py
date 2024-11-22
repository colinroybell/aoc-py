import pytest
from ec2024.day13 import Run_2024_13


class Test_2024_13:
    def setup_class(self):
        self.day = Run_2024_13()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 28

    def test_bringup_3(self):
        assert self.day.run_part("3", "test2") == 14

    def test_regression_1(self):
        assert self.day.run_part("1") == 149

    def test_regression_2(self):
        assert self.day.run_part("2") == 568

    def test_regression_3(self):
        assert self.day.run_part("3") == 535
