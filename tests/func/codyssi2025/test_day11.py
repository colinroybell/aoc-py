import pytest
from codyssi2025.day11 import Run_2025_11


class Test_2025_11:
    def setup_class(self):
        self.day = Run_2025_11()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 9047685997827

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == "4iWAbo%6"

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 2366

    def test_regression_1(self):
        assert self.day.run_part("1") == 9983400664376

    def test_regression_2(self):
        assert self.day.run_part("2") == "60bUm4ygI"

    def test_regression_3(self):
        assert self.day.run_part("3") == 7240
