import pytest
from ec2025.day07 import Run_2025_07


class Test_2025_07:
    def setup_class(self):
        self.day = Run_2025_07()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == "Oroneth"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 23

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 25

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test4") == 1154

    def test_regression_1(self):
        assert self.day.run_part("1") == "Azadarin"

    def test_regression_2(self):
        assert self.day.run_part("2") == 2353

    def test_regression_3(self):
        assert self.day.run_part("3") == 4736127
