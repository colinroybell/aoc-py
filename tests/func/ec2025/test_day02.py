import pytest
from ec2025.day02 import Run_2025_02


class Test_2025_02:
    def setup_class(self):
        self.day = Run_2025_02()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == "[357,862]"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 4076

    def test_bringup_3(self):
        assert self.day.run_part("3", "test2") == 406954

    def test_regression_1(self):
        assert self.day.run_part("1") == "[237221,967434]"

    def test_regression_2(self):
        assert self.day.run_part("2") == 1154

    def test_regression_3(self):
        assert self.day.run_part("3") == 108057
