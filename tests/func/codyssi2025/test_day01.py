import pytest
from codyssi2025.day01 import Run_2025_01


class Test_2025_01:
    def setup_class(self):
        self.day = Run_2025_01()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 21

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 23

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 189

    def test_regression_1(self):
        assert self.day.run_part("1") == -132

    def test_regression_2(self):
        assert self.day.run_part("2") == -124

    def test_regression_3(self):
        assert self.day.run_part("3") == -874
