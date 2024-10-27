import pytest
from aoc2015.day12 import Run_2015_12


class Test_2015_12:
    def setup_class(self):
        self.day = Run_2015_12()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["[1,2,3]"]) == 6

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ['{"a":2,"b":4}']) == 6

    def test_bringup_a_3(self):
        assert self.day.run_part("a", ["[[[3]]]"]) == 3

    def test_bringup_a_4(self):
        assert self.day.run_part("a", ['{"a":{"b":4},"c":-1}']) == 3

    def test_bringup_a_5(self):
        assert self.day.run_part("a", ['{"a":[-1,1]}']) == 0

    def test_bringup_a_6(self):
        assert self.day.run_part("a", ['[-1,{"a":1}]']) == 0

    def test_bringup_a_7(self):
        assert self.day.run_part("a", ["[]"]) == 0

    def test_bringup_a_8(self):
        assert self.day.run_part("a", ["{}"]) == 0

    def test_bringup_b_1(self):
        assert self.day.run_part("b", ["[1,2,3]"]) == 6

    def test_bringup_b_2(self):
        assert self.day.run_part("b", ['[1,{"c":"red","b":2},3]']) == 4

    def test_bringup_b_3(self):
        assert self.day.run_part("b", ['{"d":"red","e":[1,2,3,4],"f":5}']) == 0

    def test_bringup_b_4(self):
        assert self.day.run_part("b", ['[1,"red",5]']) == 6

    def test_regression_a(self):
        assert self.day.run_part("a") == 119433

    def test_regression_b(self):
        assert self.day.run_part("b") == 68466
