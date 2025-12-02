import pytest
from aoc2025.day02 import Run_2025_02, is_invalid


class Test_2025_02:
    def setup_class(self):
        self.day = Run_2025_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 1227775554

    def test_bringup_invalid(self):
        assert is_invalid("11", "b")
        assert is_invalid("21212121", "b")
        assert is_invalid("1010", "b")
        assert not is_invalid("222220", "b")

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 4174379265

    def test_regression_a(self):
        assert self.day.run_part("a") == 34826702005

    def test_regression_b(self):
        assert self.day.run_part("b") == 43287141963
