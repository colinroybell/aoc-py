import pytest
from codyssi2025.day02 import Run_2025_02


class Test_2025_02:
    def setup_class(self):
        self.day = Run_2025_02()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 9130674516975

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 1000986169836015

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 5496

    def test_regression_1(self):
        assert self.day.run_part("1") == 11417002989774

    def test_regression_2(self):
        assert self.day.run_part("2") == 2930335471366458630

    def test_regression_3(self):
        assert self.day.run_part("3") == 5140
