import pytest
from ec2025.day15 import Run_2025_15


class Test_2025_15:
    def setup_class(self):
        self.day = Run_2025_15()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1") == 6

    def test_bringup_1_2(self):
        assert self.day.run_part("1", "test2") == 16

    def test_regression_1(self):
        assert self.day.run_part("1") == 107

    def test_regression_2(self):
        assert self.day.run_part("2") == 3310

    def test_regression_3(self):
        assert self.day.run_part("3") == 528297907
