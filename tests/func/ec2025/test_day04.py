import pytest
from ec2025.day04 import Run_2025_04


class Test_2025_04:
    def setup_class(self):
        self.day = Run_2025_04()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1") == 32400

    def test_bringup_1_2(self):
        assert self.day.run_part("1", "test2") == 15888

    def test_bringup_2_1(self):
        assert self.day.run_part("2", "test1") == 625000000000

    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test2") == 1274509803922

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 400

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test4") == 6818

    def test_regression_1(self):
        assert self.day.run_part("1") == 20049

    def test_regression_2(self):
        assert self.day.run_part("2") == 2677651905253

    def test_regression_3(self):
        assert self.day.run_part("3") == 103502736822
