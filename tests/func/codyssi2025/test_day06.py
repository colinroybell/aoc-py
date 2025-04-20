import pytest
from codyssi2025.day06 import Run_2025_06


class Test_2025_06:
    def setup_class(self):
        self.day = Run_2025_06()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 59

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 1742

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 2708

    def test_regression_1(self):
        assert self.day.run_part("1") == 1388

    def test_regression_2(self):
        assert self.day.run_part("2") == 36474

    def test_regression_3(self):
        assert self.day.run_part("3") == 52670
