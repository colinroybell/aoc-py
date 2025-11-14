import pytest
from ecst01.day02 import Run_st01_02


class Test_st01_02:
    def setup_class(self):
        self.day = Run_st01_02()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1") == "CFGNLK"

    def test_bringup_1_2(self):
        assert self.day.run_part("1", "test2") == "EVERYBODYCODES"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test3") == "MGFLNK"

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test4") == "DJMGL"

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test5") == "DJCGL"

    def test_regression_1(self):
        assert self.day.run_part("1") == "QUACK!GXZLHBJP"

    def test_regression_2(self):
        assert self.day.run_part("2") == "QUACK!XXZGWWHJMVPXWF"

    def test_regression_3(self):
        assert self.day.run_part("3") == "QUACK!GHMRYXGVYJLMFVNGZSMPBJXNZJPR"
