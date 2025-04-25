import pytest
from codyssi2025.day14 import Run_2025_14


class Test_2025_14:
    def setup_class(self):
        self.day = Run_2025_14()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 90

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 8256

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1", budget=150) == 59388

    def test_regression_1(self):
        assert self.day.run_part("1") == 108

    def test_regression_2(self):
        assert self.day.run_part("2") == 26224

    def test_regression_3(self):
        assert self.day.run_part("3") == 468520
