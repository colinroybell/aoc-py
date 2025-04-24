import pytest
from codyssi2025.day12 import Run_2025_12


class Test_2025_12:
    def setup_class(self):
        self.day = Run_2025_12()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 18938

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 11496

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 19022

    def test_regression_1(self):
        assert self.day.run_part("1") == 20054631616

    def test_regression_2(self):
        assert self.day.run_part("2") == 123778255

    def test_regression_3(self):
        assert self.day.run_part("3") == 20534118176
