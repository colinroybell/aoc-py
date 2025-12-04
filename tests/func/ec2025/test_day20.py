import pytest
from ec2025.day20 import Run_2025_20


class Test_2025_20:
    def setup_class(self):
        self.day = Run_2025_20()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1") == 7

    def test_bringup_1_2(self):
        assert self.day.run_part("1", "test2") == 0

    def test_bringup_1_3(self):
        assert self.day.run_part("1", "test3") == 0

    def test_bringup_2(self):
        assert self.day.run_part("2", "test4") == 32

    def test_bringup_3(self):
        assert self.day.run_part("3", "test5") == 23

    def test_regression_1(self):
        assert self.day.run_part("1") == 128

    def test_regression_2(self):
        assert self.day.run_part("2") == 567

    def test_regression_3(self):
        assert self.day.run_part("3") == 464
