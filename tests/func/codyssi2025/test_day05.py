import pytest
from codyssi2025.day05 import Run_2025_05


class Test_2025_05:
    def setup_class(self):
        self.day = Run_2025_05()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 226

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 114

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 1384

    def test_regression_1(self):
        assert self.day.run_part("1") == 695

    def test_regression_2(self):
        assert self.day.run_part("2") == 125

    def test_regression_3(self):
        assert self.day.run_part("3") == 7133
