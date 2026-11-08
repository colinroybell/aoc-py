import pytest
from ec2026.day09 import Run_2026_09


class Test_2026_09:
    def setup_class(self):
        self.day = Run_2026_09()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 27

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 42

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 42

    def test_regression_1(self):
        assert self.day.run_part("1") == 202

    def test_regression_2(self):
        assert self.day.run_part("2") == 15462

    def test_regression_3(self):
        assert self.day.run_part("3") == 895116643552684
