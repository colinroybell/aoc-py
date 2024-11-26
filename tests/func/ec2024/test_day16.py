import pytest
from ec2024.day16 import Run_2024_16


class Test_2024_16:
    def setup_class(self):
        self.day = Run_2024_16()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == ">.- -.- ^,-"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1", pulls=0) == 0
        assert self.day.run_part("2", "test1", pulls=1) == 1
        assert self.day.run_part("2", "test1", pulls=2) == 2
        assert self.day.run_part("2", "test1", pulls=3) == 4
        assert self.day.run_part("2", "test1", pulls=4) == 5
        assert self.day.run_part("2", "test1", pulls=5) == 7
        assert self.day.run_part("2", "test1", pulls=10) == 15
        assert self.day.run_part("2", "test1", pulls=100) == 138
        assert self.day.run_part("2", "test1", pulls=1000) == 1383

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3", pulls=1) == "4 1"
        assert self.day.run_part("3", "test3", pulls=2) == "6 1"
        assert self.day.run_part("3", "test3", pulls=3) == "9 2"
        assert self.day.run_part("3", "test3", pulls=10) == "26 5"
        assert self.day.run_part("3", "test3", pulls=100) == "246 50"
        assert self.day.run_part("3", "test3", pulls=256) == "627 128"
        assert self.day.run_part("3", "test3", pulls=1000) == "2446 500"
        assert self.day.run_part("3", "test3", pulls=2024) == "4948 1012"

    def test_regression_1(self):
        assert self.day.run_part("1") == "*.^ <,< >,< <,>"

    def test_regression_2(self):
        assert self.day.run_part("2") == 138238937442

    def test_regression_3(self):
        assert self.day.run_part("3") == "618 82"
