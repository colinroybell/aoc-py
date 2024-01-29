import pytest
from aoc2017.day09 import Run_2017_09


class Test_2017_09:
    def setup_class(self):
        self.day = Run_2017_09()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["{}"]) == 1

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["{{{}}}"]) == 6

    def test_bringup_a_3(self):
        assert self.day.run_part("a", ["{{},{}}"]) == 5

    def test_bringup_a_4(self):
        assert self.day.run_part("a", ["{{{},{},{{}}}}"]) == 16

    def test_bringup_a_5(self):
        assert self.day.run_part("a", ["{<a>,<a>,<a>,<a>}"]) == 1

    def test_bringup_a_6(self):
        assert self.day.run_part("a", ["{{<ab>},{<ab>},{<ab>},{<ab>}}"]) == 9

    def test_bringup_a_7(self):
        assert self.day.run_part("a", ["{{<!!>},{<!!>},{<!!>},{<!!>}}"]) == 9

    def test_bringup_a_8(self):
        assert self.day.run_part("a", ["{{<a!>},{<a!>},{<a!>},{<ab>}}"]) == 3

    def test_bringup_b_1(self):
        assert self.day.run_part("b", ["<>"]) == 0

    def test_bringup_b_2(self):
        assert self.day.run_part("b", ["<random characters>"]) == 17

    def test_bringup_b_3(self):
        assert self.day.run_part("b", ["<<<<>"]) == 3

    def test_bringup_b_4(self):
        assert self.day.run_part("b", ["<{!>}>"]) == 2

    def test_bringup_b_5(self):
        assert self.day.run_part("b", ["<!!>"]) == 0

    def test_bringup_b_6(self):
        assert self.day.run_part("b", ["<!!!>>"]) == 0

    def test_bringup_b_7(self):
        assert self.day.run_part("b", ['<{o"i!a,<{i<a>']) == 10

    def test_regression_a(self):
        assert self.day.run_part("a") == 14204

    def test_regression_b(self):
        assert self.day.run_part("b") == 6622
