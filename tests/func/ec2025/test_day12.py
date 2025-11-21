import pytest
from ec2025.day12 import Run_2025_12


class Test_2025_12:
    def setup_class(self):
        self.day = Run_2025_12()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 16

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 58

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 14

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test4") == 136

    def test_regression_1(self):
        assert self.day.run_part("1") == 250

    def test_regression_2(self):
        assert self.day.run_part("2") == 5715

    def test_regression_3(self):
        assert self.day.run_part("3") == 3959
