import pytest
from ec2024.day09 import Run_2024_09


class Test_2024_09:
    def setup_class(self):
        self.day = Run_2024_09()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 10

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 10

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 10449

    def test_regression_1(self):
        assert self.day.run_part("1") == 12063

    def test_regression_2(self):
        assert self.day.run_part("2") == 5015

    def test_regression_3(self):
        assert self.day.run_part("3") == 152079
