import pytest
from ec2026.day07 import Run_2026_07


class Test_2026_07:
    def setup_class(self):
        self.day = Run_2026_07()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 102

    def test_bringup_2_1(self):
        assert self.day.run_part("2", "test1") == 1316

    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test2") == 1214633

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test1", explosion_limit=100) == 187

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test3") == 34777023

    def test_regression_1(self):
        assert self.day.run_part("1") == 290

    def test_regression_2(self):
        assert self.day.run_part("2") == 121040539

    def test_regression_3(self):
        assert self.day.run_part("3") == 36578016
