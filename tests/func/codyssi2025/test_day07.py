import pytest
from codyssi2025.day07 import Run_2025_07


class Test_2025_07:
    def setup_class(self):
        self.day = Run_2025_07()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 45

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 796

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 827

    def test_regression_1(self):
        assert self.day.run_part("1") == 49406

    def test_regression_2(self):
        assert self.day.run_part("2") == 44063

    def test_regression_3(self):
        assert self.day.run_part("3") == 21844
