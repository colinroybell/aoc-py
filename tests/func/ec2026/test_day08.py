import pytest
from ec2026.day08 import Run_2026_08


class Test_2026_08:
    def setup_class(self):
        self.day = Run_2026_08()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 32

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 187

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 899889

    def test_regression_1(self):
        assert self.day.run_part("1") == 174

    def test_regression_2(self):
        assert self.day.run_part("2") == 1027

    def test_regression_3(self):
        assert self.day.run_part("3") == 899156
