import pytest
from ec2026.day12 import Run_2026_12


class Test_2026_12:
    def setup_class(self):
        self.day = Run_2026_12()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 7

    def test_bringup_2_1(self):
        assert self.day.run_part("2", "test2") == 6

    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test3") == 23

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test4") == 8

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test5") == 29

    def test_bringup_3_3(self):
        assert self.day.run_part("3", "test6") == 16

    def test_regression_1(self):
        assert self.day.run_part("1") == 220

    def test_regression_2(self):
        assert self.day.run_part("2") == 1982

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
