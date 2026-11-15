import pytest
from ec2026.day11 import Run_2026_11


class Test_2026_11:
    def setup_class(self):
        self.day = Run_2026_11()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 60

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 6

    def test_bringup_3(self):
        assert self.day.run_part("3", "test2") == 854

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 9634

    def test_regression_1(self):
        assert self.day.run_part("1") == 1400

    def test_regression_2(self):
        assert self.day.run_part("2") == 1564

    def test_regression_3(self):
        assert self.day.run_part("3") == 19822
