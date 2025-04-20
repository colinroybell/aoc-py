import pytest
from codyssi2025.day03 import Run_2025_03


class Test_2025_03:
    def setup_class(self):
        self.day = Run_2025_03()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 43

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 35

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 9

    def test_regression_1(self):
        assert self.day.run_part("1") == 51619

    def test_regression_2(self):
        assert self.day.run_part("2") == 43417

    def test_regression_3(self):
        assert self.day.run_part("3") == 980
