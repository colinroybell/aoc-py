import pytest
from aoc2015.day01 import Run_2015_01


@pytest.mark.bringup
class Test_2015_01:
    def setup_class(self):
        self.day = Run_2015_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["(())"]) == 0
        assert self.day.run_part("a", ["()()"]) == 0
        assert self.day.run_part("a", ["((("]) == 3
        assert self.day.run_part("a", ["(()(()("]) == 3
        assert self.day.run_part("a", ["))((((("]) == 3
        assert self.day.run_part("a", ["())"]) == -1
        assert self.day.run_part("a", ["))("]) == -1
        assert self.day.run_part("a", [")))"]) == -3
        assert self.day.run_part("a", [")())())"]) == -3

    def test_bringup_b(self):
        assert self.day.run_part("b", [")"]) == 1
        assert self.day.run_part("b", ["()())"]) == 5

    def test_regression_a(self):
        assert self.day.run_part("a") == 280
    
    def test_regression_b(self):    
        assert self.day.run_part("b") == 1797