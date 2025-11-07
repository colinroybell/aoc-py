import pytest
from ec2025.day03 import Run_2025_03


class Test_2025_03:
    def setup_class(self):
        self.day = Run_2025_03()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 29

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 781

    def test_bringup_3(self):
        assert self.day.run_part("3", "test2") == 3

    def test_regression_1(self):
        assert self.day.run_part("1") == 2383

    def test_regression_2(self):
        assert self.day.run_part("2") == 260

    def test_regression_3(self):
        assert self.day.run_part("3") == 2413
