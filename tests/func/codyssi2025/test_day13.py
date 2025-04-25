import pytest
from codyssi2025.day13 import Run_2025_13


class Test_2025_13:
    def setup_class(self):
        self.day = Run_2025_13()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 36

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 44720

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 18

    def test_regression_1(self):
        assert self.day.run_part("1") == 2366

    def test_regression_2(self):
        assert self.day.run_part("2") == 3936600

    def test_regression_3(self):
        assert self.day.run_part("3") == 354
