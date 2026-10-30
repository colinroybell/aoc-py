import pytest
from ec2026.day03 import Run_2026_03


class Test_2026_03:
    def setup_class(self):
        self.day = Run_2026_03()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 1478

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 1161463

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 50987

    def test_regression_1(self):
        assert self.day.run_part("1") == 12653

    def test_regression_2(self):
        assert self.day.run_part("2") == 25859750097

    def test_regression_3(self):
        assert self.day.run_part("3") == 367025
