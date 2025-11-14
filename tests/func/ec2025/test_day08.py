import pytest
from ec2025.day08 import Run_2025_08


class Test_2025_08:
    def setup_class(self):
        self.day = Run_2025_08()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1", nails=8) == 4

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2", nails=8) == 21

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 7

    def test_regression_1(self):
        assert self.day.run_part("1") == 55

    def test_regression_2(self):
        assert self.day.run_part("2") == 2924365

    def test_regression_3(self):
        assert self.day.run_part("3") == 2787
