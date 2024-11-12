import pytest
from ec2024.day06 import Run_2024_06


class Test_2024_06:
    def setup_class(self):
        self.day = Run_2024_06()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == "RRB@"

    def test_regression_1(self):
        assert self.day.run_part("1") == "RRXKQXBSGRMW@"

    def test_regression_2(self):
        assert self.day.run_part("2") == "RKRMFGBPJB@"

    def test_regression_3(self):
        assert self.day.run_part("3") == "RRPMJQRFPDTZ@"
