import pytest
from codyssi2025.day04 import Run_2025_04


class Test_2025_04:
    def setup_class(self):
        self.day = Run_2025_04()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 1247

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 219

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 539

    def test_regression_1(self):
        assert self.day.run_part("1") == 138797

    def test_regression_2(self):
        assert self.day.run_part("2") == 27867

    def test_regression_3(self):
        assert self.day.run_part("3") == 46535
