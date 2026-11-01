import pytest
from ec2026.day05 import Run_2026_05


class Test_2026_05:
    def setup_class(self):
        self.day = Run_2026_05()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 137

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 69

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 14

    def test_regression_1(self):
        assert self.day.run_part("1") == 1041

    def test_regression_2(self):
        assert self.day.run_part("2") == 1091

    def test_regression_3(self):
        assert self.day.run_part("3") == 9258
