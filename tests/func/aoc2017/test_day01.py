import pytest
from aoc2017.day01 import Run_2017_01


class Test_2017_01:
    def setup_class(self):
        self.day = Run_2017_01()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["1122"]) == 3

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["1111"]) == 4

    def test_bringup_a_3(self):
        assert self.day.run_part("a", ["1234"]) == 0

    def test_bringup_a_4(self):
        assert self.day.run_part("a", ["91212129"]) == 9

    def test_bringup_b_1(self):
        assert self.day.run_part("b", ["1212"]) == 6

    def test_bringup_b_2(self):
        assert self.day.run_part("b", ["1221"]) == 0

    def test_bringup_b_3(self):
        assert self.day.run_part("b", ["123425"]) == 4

    def test_bringup_b_4(self):
        assert self.day.run_part("b", ["123123"]) == 12

    def test_bringup_b_5(self):
        assert self.day.run_part("b", ["12131415"]) == 4

    def test_regression_a(self):
        assert self.day.run_part("a") == 1158

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 1132
