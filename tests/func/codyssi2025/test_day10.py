import pytest
from codyssi2025.day10 import Run_2025_10


class Test_2025_10:
    def setup_class(self):
        self.day = Run_2025_10()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 73

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 94

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 120

    def test_regression_1(self):
        assert self.day.run_part("1") == 208

    def test_regression_2(self):
        assert self.day.run_part("2") == 84

    def test_regression_3(self):
        assert self.day.run_part("3") == 293
