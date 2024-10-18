import pytest
from aoc2020.day18 import Run_2020_18


class Test_2020_18:
    def setup_class(self):
        self.day = Run_2020_18()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 71

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 51

    def test_bringup_a_3(self):
        assert self.day.run_part("a", "test3") == 26

    def test_bringup_a_4(self):
        assert self.day.run_part("a", "test4") == 437

    def test_bringup_a_5(self):
        assert self.day.run_part("a", "test5") == 12240

    def test_bringup_a_6(self):
        assert self.day.run_part("a", "test6") == 13632

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 231

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test2") == 51

    def test_bringup_b_3(self):
        assert self.day.run_part("b", "test3") == 46

    def test_bringup_b_4(self):
        assert self.day.run_part("b", "test4") == 1445

    def test_bringup_b_5(self):
        assert self.day.run_part("b", "test5") == 669060

    def test_bringup_b_6(self):
        assert self.day.run_part("b", "test6") == 23340

    def test_regression_a(self):
        assert self.day.run_part("a") == 8298263963837

    def test_regression_b(self):
        assert self.day.run_part("b") == 145575710203332
